def try_me(your_question):
    if '?' in your_question:
        return 'Silly question, go to work!'

if __name__ == "__main__":
    your_question = 'hello?'
    print(try_me(your_question))

    # Le Wagon location
    #lat1, lon1 = 48.865070, 2.380009
    #Insert your coordinates from google maps here
    #lat2, lon2 = 52.337589, 4.871825
    #distance = haversine(lon1, lat1, lon2, lat2)
    #print(distance)
