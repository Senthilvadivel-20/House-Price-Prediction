from django.shortcuts import render
from House_price import data
import joblib

def Home(request):
    return render(request,'Home.html')



def result(request):

    chennai=joblib.load('.\Files\Chennai_price_model.sav')

    Location_value=request.GET["Location"]
    Location=data.locatio_encoder(Location_value)
    Area=request.GET["Area"]
    No_of_Bedrooms=request.GET["No. of Bedrooms"]   #Changed
    Resale=request.GET["Resale"]
    MaintenanceStaff=request.GET["MaintenanceStaff"]
    Gymnasium=request.GET["Gymnasium"]
    SwimmingPool=request.GET["SwimmingPool"]
    LandscapedGardens=request.GET["LandscapedGardens"]
    JoggingTrack=request.GET["JoggingTrack"]
    RainWaterHarvesting=request.GET["RainWaterHarvesting"]
    IndoorGames=request.GET["IndoorGames"]
    ShoppingMall=request.GET["ShoppingMall"]
    Intercom=request.GET["Intercom"]
    SportsFacility=request.GET["SportsFacility"]
    ATM=request.GET["ATM"]
    ClubHouse=request.GET["ClubHouse"]
    School=request.GET["School"]
    _24X7Security=request.GET["24X7Security"]   #changed
    PowerBackup=request.GET["PowerBackup"]
    CarParking=request.GET["CarParking"]
    StaffQuarter=request.GET["StaffQuarter"]
    Cafeteria=request.GET["Cafeteria"]
    MultipurposeRoom=request.GET["MultipurposeRoom"]
    Hospital=request.GET["Hospital"]
    WashingMachine=request.GET["WashingMachine"]
    Gasconnection=request.GET["Gasconnection"]
    AC=request.GET["AC"]
    Wifi=request.GET["Wifi"]
    Children_playarea=request.GET["Children playarea"] ###Changed
    LiftAvailable=request.GET["LiftAvailable"]
    BED=request.GET["BED"]
    VaastuCompliant=request.GET["VaastuCompliant"]
    Microwave=request.GET["Microwave"]
    GolfCourse=request.GET["GolfCourse"]
    TV=request.GET["TV"]
    DiningTable=request.GET["DiningTable"]
    Sofa=request.GET["Sofa"]
    Wardrobe=request.GET["Wardrobe"]
    Refrigerator=request.GET["Refrigerator"]
    
    predictor=[Location,Area,No_of_Bedrooms,Resale,MaintenanceStaff,Gymnasium,SwimmingPool,
                LandscapedGardens,JoggingTrack,RainWaterHarvesting,IndoorGames,ShoppingMall,Intercom,
                SportsFacility,ATM,ClubHouse,School,_24X7Security,PowerBackup,
                CarParking,StaffQuarter,Cafeteria,MultipurposeRoom,Hospital,WashingMachine,
                Gasconnection,AC,Wifi,Children_playarea,LiftAvailable,BED,VaastuCompliant,
                Microwave,GolfCourse,TV,DiningTable,Sofa,Wardrobe,Refrigerator,]

    price=chennai.predict([predictor])[0]

    price=round(price)

    return render(request,'result.html',locals())

    