from app import app,config_obj










if __name__=="__main__":
    app.run(debug=config_obj.DEBUG,host=config_obj.HOST,port=config_obj.SERVER_PORT)




