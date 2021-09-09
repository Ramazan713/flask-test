from app import app,cache,dbManager,config_obj,log_config_file
from flask import jsonify,make_response,request,abort
import os,yaml,logging,logging.config
from werkzeug.exceptions import HTTPException


with open(log_config_file,"r") as f:
    logging.config.dictConfig(yaml.safe_load(f.read()))


logger=logging.getLogger(__name__)


@app.route("/",methods=["GET"])
@cache.cached(timeout=config_obj.CACHE_TIMEOUT)
def index():
    return make_response(jsonify(dbManager.getAllUser()),200)


@app.route("/name/<name>",methods=["GET"])
@cache.cached(timeout=config_obj.CACHE_TIMEOUT)
def userSearchWithName(name:str):
    result=dbManager.getUserWithName(name)
    if result:
        return make_response(jsonify(result))
    else:
        abort(404,"the user you looking for has not found")

@app.route("/surname/<surname>",methods=["GET"])
@cache.cached(timeout=config_obj.CACHE_TIMEOUT)
def userSearchWithSurname(surname:str):
    result=dbManager.getUserWithSurname(surname)
    if result:
        return make_response(jsonify(result))
    else:
        abort(404,"the user you looking for has not found")
        

@app.route("/append",methods=["GET"])
def appendUser():
    name=request.args["name"]
    surname=request.args["surname"]
    dbManager.insertUser(name,surname)
    return "success"

@app.route("/delete/<value>",methods=["GET"])
def deleteUser(value:str):
    print("valll:",value)
    key=request.args.get("key",None)
    if key=="name":
        if not isinstance(value,str):
            abort(404,"must be str for name (key:name)")
        result=dbManager.deleteUserWithName(value)
    elif key=="surname":
        if not isinstance(value,str):
            abort(404,"must be str for surname (key:surname)")
        result=dbManager.deleteUserWithSurname(value)
    else:
        if not value.isdigit():
            abort(404,"must be int for uid")
        result=dbManager.deleteUserWithUid(value)

    return make_response(jsonify(result))

@app.errorhandler(HTTPException)
def http_exception_handler(e:HTTPException):
    error_body={
            "name":e.name,
            "code":e.code,
            "description":e.description,   
        }
    logger.error(e)
    return make_response(jsonify(error_body),e.code)

@app.errorhandler(Exception)
def handle_exception(e:Exception):
    code=500
    error_body="some errors occured"
    logger.critical(e,exc_info=True)
    return make_response(error_body,code)