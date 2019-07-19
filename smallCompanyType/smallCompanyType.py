from keras.models import load_model
import numpy as np
from os import path
import pickle



class SmallCompanyType():
    
    inverse_transform={0: 'Acupuncturist', 1: 'Adult Entertainment Store', 2: 'Animal Clinic/Hospital', 3: 'Animal Services', 4: 'Artist', 5: 'Artist Live/Work Studio', 6: 'Assembly Hall', 7: 'Auctioneer', 8: 'Auto Dealer', 9: 'Auto Detailing', 10: 'Auto Painter & Body Shop', 11: 'Auto Parking Lot/Parkade', 12: 'Auto Repairs', 13: 'Auto Washer', 14: 'Auto Wholesaler', 15: 'Beauty Services', 16: 'Bed and Breakfast', 17: 'Boat Charter Services', 18: 'Booking Agency', 19: 'Boot & Shoe Repairs', 20: 'Business Services', 21: 'Carpet/Upholstery Cleaner', 22: 'Caterer', 23: 'Club', 24: 'Community Association', 25: 'Computer Services', 26: 'Contractor', 27: 'Contractor - Special Trades', 28: 'Cosmetologist', 29: 'Dance Hall', 30: 'Dating Services', 31: 'ESL Instruction', 32: 'Educational', 33: 'Electrical Contractor', 34: 'Electrical-Security Alarm Installation', 35: 'Employment Agency', 36: 'Entertainment Services', 37: 'Equipment Operator', 38: 'Exhibitions/Shows/Concerts', 39: 'Financial Institution', 40: 'Financial Services', 41: 'Fitness Centre', 42: 'Food Processing', 43: 'Gas Contractor', 44: 'Gasoline Station', 45: 'Hair Stylist/Hairdresser', 46: 'Health Services', 47: 'Health and Beauty', 48: 'Home Business', 49: 'Homecraft', 50: 'Hotel', 51: 'Instruction', 52: 'Janitorial Services', 53: 'Jeweller', 54: 'Laboratory', 55: 'Landscape Gardener', 56: 'Late Night Dance Event', 57: 'Laundry', 58: 'Liquor Equipment', 59: 'Liquor Establishment', 60: 'Liquor License Application', 61: 'Liquor Retail Store', 62: 'Locksmith', 63: 'Manufacturer', 64: 'Manufacturer - Food', 65: 'Marina Operator', 66: 'Marine Services', 67: 'Massage Therapist', 68: 'Money Services', 69: 'Moving/Transfer Service', 70: 'Non-profit Housing', 71: 'Office', 72: 'Painter', 73: 'Pawnbroker', 74: 'Personal Care Home', 75: 'Personal Services', 76: 'Pest Control/Exterminator', 77: 'Pet Store', 78: 'Photo Services', 79: 'Photographer', 80: 'Physical Therapist', 81: 'Plumber', 82: 'Plumber & Gas Contractor', 83: 'Plumber & Sprinkler Contractor', 84: 'Plumber Sprinkler & Gas Contractor', 85: 'Postal Rental Agency', 86: 'Power/ Pressure Washing', 87: 'Printing Services', 88: 'Product Assembly', 89: 'Production Company', 90: 'Property Management', 91: 'Psychic/Fortune Teller', 92: 'Real Estate Dealer', 93: 'Recycling Depot', 94: 'Referral Services', 95: 'Rentals', 96: 'Repair/ Service/Maintenance', 97: 'Residential/Commercial', 98: 'Restaurant', 99: 'Retail Dealer', 100: 'Retail Dealer - Food', 101: 'Retail Dealer - Grocery', 102: 'Roofer', 103: 'Rooming House', 104: 'Scavenging', 105: 'School (Business & Trade)', 106: 'School (Private)', 107: 'Seamstress/Tailor', 108: 'Secondary Suite - Permanent', 109: 'Secondhand Dealer', 110: 'Security Services', 111: 'Social Escort Services', 112: 'Soliciting For Charity', 113: 'Sprinkler Contractor', 114: 'Studio', 115: 'Talent Agency', 116: 'Tanning Salon', 117: 'Tattoo Parlour', 118: 'Telecommunications', 119: 'Theatre', 120: 'Therapeutic Touch Technique', 121: 'Travel Agent', 122: 'Venue', 123: 'Warehouse Operator', 124: 'Wholesale  Dealer', 125: 'Wholesale Dealer - Food', 126: 'Window Cleaner'}
    
    typeDict= { 'Acupuncturist'			:'B2C',
                'Adult Entertainment Store'	:'B2C',
                'Animal Clinic/Hospital'	:'B2C',
                'Animal Services'		:'B2C',
                'Artist'			:'B2BC',
                'Artist Live/Work Studio'	:'B2BC',
                'Assembly Hall'			:'PUB',
                'Auctioneer'			:'B2BC',
                'Auto Dealer'			:'B2BC',
                'Auto Detailing'		:'B2C',
                'Auto Painter & Body Shop'	:'B2C',
                'Auto Parking Lot/Parkade'	:'B2C',
                'Auto Repairs'			:'B2C',
                'Auto Washer'			:'B2C',
                'Auto Wholesaler'		:'B2B',
                'Beauty Services'		:'B2C',
                'Bed and Breakfast'		:'B2C',
                'Boat Charter Services'		:'B2BC',
                'Booking Agency'		:'B2BC',
                'Boot & Shoe Repairs'		:'B2C',
                'Business Services'		:'B2B',
                'Carpet/Upholstery Cleaner'	:'B2BC',
                'Caterer'			:'B2BC',
                'Club'				:'B2BC',
                'Community Association'		:'PUB',
                'Computer Services'		:'B2BC',
                'Contractor'			:'B2BC',
                'Contractor - Special Trades'	:'B2BC',
                'Cosmetologist'			:'B2C',
                'Dance Hall'			:'B2C',
                'Dating Services'		:'B2C',
                'ESL Instruction'		:'B2C',
                'Educational'			:'PUB',
                'Electrical Contractor'		:'B2BC',
                'Electrical-Security Alarm Installation' :'B2BC',
                'Employment Agency'		:'B2BC',
                'Entertainment Services'	:'B2BC',
                'Equipment Operator'		:'B2BC',
                'Exhibitions/Shows/Concerts'	:'B2BC',
                'Financial Institution'		:'B2BC',
                'Financial Services'		:'B2BC',
                'Fitness Centre'		:'B2C',
                'Food Processing'		:'B2B',
                'Gas Contractor'		:'B2BC',
                'Gasoline Station'		:'B2C',
                'Hair Stylist/Hairdresser'	:'B2C',
                'Health Services'		:'B2C',
                'Health and Beauty'		:'B2C',
                'Home Business'			:'B2BC',
                'Homecraft'			:'B2B',
                'Hotel'				:'B2BC',
                'Instruction'			:'B2BC',
                'Janitorial Services'		:'B2B',
                'Jeweller'			:'B2C',
                'Laboratory'			:'B2B',
                'Landscape Gardener'		:'B2BC',
                'Late Night Dance Event'	:'B2C',
                'Laundry'			:'B2C',
                'Liquor Equipment'		:'B2B',
                'Liquor Establishment'		:'B2C',
                'Liquor License Application'	:'B2C',
                'Liquor Retail Store'		:'B2C',
                'Locksmith'			:'B2BC',
                'Manufacturer'			:'B2B',
                'Manufacturer - Food'		:'B2B',
                'Marina Operator'		:'B2BC',
                'Marine Services'		:'B2BC',
                'Massage Therapist'		:'B2C',
                'Money Services'		:'B2BC',
                'Moving/Transfer Service'	:'B2BC',
                'Non-profit Housing'		:'PUB',
                'Office'			:'B2BC',
                'Painter'			:'B2BC',
                'Pawnbroker'			:'B2C',
                'Personal Care Home'		:'B2C',
                'Personal Services'		:'B2C',
                'Pest Control/Exterminator'	:'B2BC',
                'Pet Store'			:'B2C',
                'Photo Services'		:'B2C',
                'Photographer'			:'B2BC',
                'Physical Therapist'		:'B2C',
                'Plumber'			:'B2BC',
                'Plumber & Gas Contractor'	:'B2BC',
                'Plumber & Sprinkler Contractor':'B2BC',
                'Plumber Sprinkler & Gas Contractor':'B2BC',
                'Postal Rental Agency'		:'B2BC',
                'Power/ Pressure Washing'	:'B2BC',
                'Printing Services'		:'B2BC',
                'Product Assembly'		:'B2B',
                'Production Company'		:'B2BC',
                'Property Management'		:'B2BC',
                'Psychic/Fortune Teller'	:'B2C',
                'Real Estate Dealer'		:'B2BC',
                'Recycling Depot'		:'PUB',
                'Referral Services'		:'B2BC',
                'Rentals'			:'B2BC',
                'Repair/ Service/Maintenance'	:'B2BC',
                'Residential/Commercial'	:'B2BC',
                'Restaurant'			:'B2C',
                'Retail Dealer'			:'B2C',
                'Retail Dealer - Food'		:'B2C',
                'Retail Dealer - Grocery'	:'B2C',
                'Roofer'			:'B2BC',
                'Rooming House'			:'PUB',
                'Scavenging'			:'B2BC',
                'School (Business & Trade)'	:'PUB',
                'School (Private)'		:'PUB',
                'Seamstress/Tailor'		:'B2C',
                'Secondary Suite - Permanent'	:'B2B',
                'Secondhand Dealer'		:'B2C',
                'Security Services'		:'B2BC',
                'Social Escort Services'	:'B2C',
                'Soliciting For Charity'	:'PUB',
                'Sprinkler Contractor'		:'B2BC',
                'Studio'			:'B2BC',
                'Talent Agency'			:'B2BC',
                'Tanning Salon'			:'B2C',
                'Tattoo Parlour'		:'B2C',
                'Telecommunications'		:'B2BC',
                'Theatre'			:'B2C',
                'Therapeutic Touch Technique'	:'B2C',
                'Travel Agent'			:'B2BC',
                'Venue'				:'B2BC',
                'Warehouse Operator'		:'B2B',
                'Wholesale  Dealer'		:'B2B',
                'Wholesale Dealer - Food'	:'B2B',
                'Window Cleaner'		:'B2BC'}
    
    # Load the model components
    def __init__(self):
        models_dir = path.join(path.dirname(__file__), 'models')
        self.dnn_model = load_model(models_dir+'/company_classifier.h5')
        with open(models_dir+ '/encode.pkl','rb') as infile:
            self.enc = pickle.load(infile)
            infile.close()
    
    #Get a one-hot encoding for a company name string
    def getCompanyEncoding(self, name):
        row = np.zeros(300)
        for i in range(len(name)):
            row[i]=ord(name[i])
        #clip if too long
        row = row[:30]
        #extend if too short
        nrow = np.zeros(30)
        for i in range(30):
            nrow[i]=row[i]
        #add a dimension
        nrow=nrow[np.newaxis,:]
        test_tensor = self.enc.transform(nrow)
        return test_tensor
    
    # Predict and return a categorical label for an input company name string
    def getCompanySubtype(self, name):
        sample=self.getCompanyEncoding(name)
        predicted = (self.dnn_model.predict(sample)[0])
        return self.inverse_transform[np.argmax(predicted)]
    
    
    # Predict and return a categorical label for an input company name string
    def getCompanyType(self, name):
        return self.typeDict[self.getCompanySubtype(name)]
        
  
