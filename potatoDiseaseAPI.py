model.load('potatoDisease.h5')

img_path = 'D:/liqteq/Machine Learning/potatodiseaserecognition/test/potato_healthy/774875d3-438a-4305-afe2-7d59e2925dc4___RS_HL 1759.jpg'    # dog

pred = model.predict(new_image)
