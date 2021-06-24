
from Info import *
import asyncio

async def sahayak(message) :
    M = message.split("#")
    AgeChoice = M[1].replace(" ","")
    StateName = M[2].replace(" ","")
    CityName = M[3].replace(" ","")
    VaccineType = M[4].replace(" ","")
    VaccineDose = int(M[5].replace(" ",""))
    ## print(AgeChoice + " " + StateName + " " + CityName + " " + VaccineType + " " + str(VaccineDose))



    from selenium import webdriver
    from selenium.common.exceptions import NoSuchElementException
    import time
    from time import sleep
    from datetime import datetime, timedelta
    import os



    from bs4 import BeautifulSoup



    def Split(lst):
        return (lst[0].split())



    class DoseList:
        def __init__(self, Status,Vaccine, Dose1, Dose2):
            self.Status = Status
            self.Vaccine = Vaccine
            self.Dose1 = Dose1
            self.Dose2 = Dose2 



    def CheckStatus(s) :
        if s[0] == 'N' :
            return "NA"
        elif s[0] == 'B' :
            return "Booked"
        elif s[0] == 'D' :
            return "Dose"



    class SearchResult :
        def __init__(self,NoOfSlots,SlotInfo) :
            self.NoOfSlots = NoOfSlots
            self.SlotInfo = SlotInfo
            
        



    class DoseSearch :
        def __init__(self,Date,NoOfSlots) :
            self.Date = Date
            self.NoOfSlots = NoOfSlots
            



    class SearchTemplate :
        def __init__(self,HospitalName,HospitalAdress,Dose) :
            self.HospitalName = HospitalName
            self.HospitalAdress = HospitalAdress
            self.Dose = Dose



    # ChromeDriver Link :
    # https://chromedriver.chromium.org/downloads


    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path="chromedriver", options=options)

    driver.get("https://www.cowin.gov.in/home")

    TabbedSearch = driver.find_elements_by_xpath('//*[@id="mat-tab-label-0-1"]/div')
    TabbedSearch[0].click()


    await asyncio.sleep(0.1)
    SearchState = driver.find_elements_by_xpath('//*[@id="mat-select-value-1"]/span')
    SearchState[0].click()


    StateNo = InfoState(StateName.upper())
    R = []
    if(StateNo == "-1") :
        driver.quit()
        return R
    CityNo = InfoCity(CityName)
    if(CityNo == "-1") :
        R.append("City Not found")
        driver.quit()
        return R

# //*[@id="mat-option-37"]

    await asyncio.sleep(0.5)
    SelectState = driver.find_element_by_xpath('//*[@id="mat-option-' + StateNo + '"]')
    # SelectState = driver.find_element_by_id("mat-option-"+StateNo)
    SelectState.click()

    await asyncio.sleep(0.1)
    SearchCity = driver.find_element_by_xpath('//*[@id="mat-select-2"]')
    SearchCity.click()

    await asyncio.sleep(0.1)
    tempHTML = driver.page_source
    soup = BeautifulSoup(tempHTML,'html.parser')
    flag = 0
    pos = 1
    for p in soup.find_all("span",class_ = "mat-option-text") :
        tempstr = p.get_text()
        # print(tempstr)
        if (CityName.replace(" ","")).upper() == (tempstr.replace(" ","")).upper() :
            # print("\n" + tempstr+ "\n")
            flag = 1
            break
        else :
            pos = pos + 1
    if flag == 0 :
        R.append("City Not Found")
        return R
    else :
        pos = pos + 37
        
    print(pos)


    await asyncio.sleep(0.1)
    SelectCity = driver.find_element_by_xpath('//*[@id="mat-option-' + str(pos-1) + '"]')
    # SelectCity = driver.find_element_by_id("mat-option-"+ str(pos-1))
    SelectCity.click()



    await asyncio.sleep(0.1)
    SubmitButton = driver.find_element_by_xpath('//*[@id="mat-tab-content-0-1"]/div/div/div[3]/button')
    SubmitButton.click()



    # To get 18+ data 
    await asyncio.sleep(0.1)
    # Age18 = driver.find_element_by_xpath('/html/body/app-root/div/app-home/div[3]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[1]/div[1]/div/div[1]/label')
    Age18 = driver.find_element_by_xpath('/html/body/app-root/div/app-home/div[3]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div[1]/div/div[1]')
    Age18.click()


    await asyncio.sleep(0.1)
    Age18 = driver.page_source
    soup = BeautifulSoup(Age18,'html.parser')

    indicator = []
    itr=0
    i = 0
    Address18 =  []
    for p in soup.find_all("p",class_ = "center-name-text") :
        s= p.get_text()
        if s[0] == ' ' :
            flag = 1
            for j in range(0,len(Address18)) :
                if s.replace(" ","") in Address18[j].replace(" ","") :
                    flag = 0
                    indicator.append(itr)
                    break
            if flag == 1 :
                # print(s)
                Address18.append(s)
                i = i + 1
        itr = itr + 1
    # print(i)



    i = 0
    itr = 0
    HospitalName18 = []
    for p in soup.find_all("h5",class_ = "center-name-title") :
        s= p.get_text()
        if s[0] == ' ' :
            flag = 1 
            for j in range(0,len(indicator)) :
                if itr == indicator[j] :
                    flag = 0 
                    break
            if flag == 1 :
                HospitalName18.append(s)
                # print(s)
                i = i + 1
        itr = itr + 1 
    # print(i)

    i = 0
    DoseAvailability18 = []
    for p in soup.find_all("div",class_ = "slot-available-main") :
    # for p in soup.find_all("div",class_ = "slots-box") :
        s= p.get_text()
        DoseAvailability18.append(s)
        i = i + 1
    # print(i)

    i = 0
    ##print(len(DoseAvailability18))
    for i in range(0,len(DoseAvailability18)) :
        DoseAvailability18[i] = DoseAvailability18[i].replace("Age 18+","")
        if DoseAvailability18[i][0] == ' ' :
            DoseAvailability18[i] = DoseAvailability18[i].replace(" ","",1)
        # print(DoseAvailability18[i])
        i = i + 1
    # print(i) 


    global DoseData18
    DoseData18 = []
    # print(len(DoseAvailability18)) 
    # print(len(HospitalName18))
    for i in range(0,len(DoseAvailability18)) :
        k=0
        DoseString = DoseAvailability18[i]
        list = [DoseString]
        # ##print(Split(list)[0])
        InfoList = []
        for j in range(0,7) :
            InitialStatus = CheckStatus(Split(list)[k])
            if InitialStatus == "Booked" :
                D = DoseList("Booked",Split(list)[k+1],"-1","-1")
                InfoList.append(D)
                k = k + 2
            elif InitialStatus == "NA" :
                D = DoseList("NA","-1","-1","-1")
                InfoList.append(D)
                k = k + 1
            elif InitialStatus == "Dose" :
                D = DoseList("Available",Split(list)[k+5],Split(list)[k+1],Split(list)[k+4])
                InfoList.append(D)
                k = k + 6
        DoseData18.append(InfoList)

    def SearchDose18(DoseNumber,DoseType):
        Count =  0
        List = []
        for i in range(0,len(HospitalName18)) :
            flag = 0
            Info = []
            # print(len(DoseData18))
            for j in range(0,len(DoseData18[i])) :
                if DoseData18[i][j].Status == "Available" :
                    if DoseData18[i][j].Vaccine == DoseType :
                        if DoseNumber == 1 :
                            if DoseData18[i][j].Dose1 != "-1" and DoseData18[i][j].Dose1.replace(" ","") != "0" :
                                flag = 1 
                                date = str(datetime.today() + timedelta(j))
                                Info.append(DoseSearch(date[0:10],DoseData18[i][j].Dose1))
                                ##print(j)
                        elif DoseNumber == 2 :
                            if DoseData18[i][j].Dose2 != "-1" and DoseData18[i][j].Dose2.replace(" ","") != "0":
                                flag = 1 
                                date = str(datetime.today() + timedelta(j))
                                Info.append(DoseSearch(date[0:10],DoseData18[i][j].Dose2))
                                ##print(HospitalName18[i])
            if flag == 1 :
                Count = Count + 1 
                List.append(SearchTemplate(HospitalName18[i],Address18[i],Info))
        return SearchResult(Count,List)



    # To get 18+ data 
    await asyncio.sleep(0.1)
    # Age18 = driver.find_element_by_xpath('/html/body/app-root/div/app-home/div[3]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[1]/div[1]/div/div[1]/label')
    Age18 = driver.find_element_by_xpath('/html/body/app-root/div/app-home/div[3]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div[1]/div/div[1]')


    Age18.click()



    # To get 45+ data 
    await asyncio.sleep(0.1)
    Age45 = driver.find_element_by_xpath('/html/body/app-root/div/app-home/div[3]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div[1]/div/div[2]')
    Age45.click()

    Age45 = driver.page_source
    soup = BeautifulSoup(Age45,'html.parser')

    indicator = []
    itr = 0
    i = 0
    Address45 =  []
    for p in soup.find_all("p",class_ = "center-name-text") :
        s= p.get_text()
        if s[0] == ' ' :
            flag = 1
            for j in range(0,len(Address45)) :
                if s.replace(" ","") in Address45[j].replace(" ","") :
                    flag = 0
                    indicator.append(itr)
                    break
            if flag == 1 :
                # print(s)
                Address45.append(s)
                i = i + 1
        itr = itr + 1
            
    ##print(i)


    itr = 0
    i = 0
    HospitalName45 = []
    for p in soup.find_all("h5",class_ = "center-name-title") :
        s= p.get_text()
        if s[0] == ' ' :
            flag = 1 
            for j in range(0,len(indicator)) :
                if itr == indicator[j] :
                    flag = 0 
                    break
            if flag == 1 :
                HospitalName45.append(s)
                # print(s)
                i = i + 1
        itr = itr + 1 
    ##print(i)

    i = 0
    DoseAvailability45 = []
    for p in soup.find_all("div",class_ = "slot-available-main") :
        s= p.get_text()
        # if s[0] == ' ' :
        DoseAvailability45.append(s)
        i = i + 1
    ##print(i)

    i = 0
    ##print(len(DoseAvailability45))
    for i in range(0,len(DoseAvailability45)) :
        DoseAvailability45[i] = DoseAvailability45[i].replace("Age 45+","")
        if DoseAvailability45[i][0] == ' ' :
            DoseAvailability45[i] = DoseAvailability45[i].replace(" ","",1)
        ##print(DoseAvailability45[i])
        i = i + 1
    ##print(i) 

    DoseData = []
    for i in range(0,len(DoseAvailability45)) :
        k=0
        DoseString = DoseAvailability45[i]
        list = [DoseString]
        ##print(Split(list)[0])
        InfoList = []
        for j in range(0,7) :
            InitialStatus = CheckStatus(Split(list)[k])
            if InitialStatus == "Booked" :
                D = DoseList("Booked",Split(list)[k+1],"-1","-1")
                InfoList.append(D)
                k = k + 2
            elif InitialStatus == "NA" :
                D = DoseList("NA","-1","-1","-1")
                InfoList.append(D)
                k = k + 1
            elif InitialStatus == "Dose" :
                D = DoseList("Available",Split(list)[k+5],Split(list)[k+1],Split(list)[k+4])
                InfoList.append(D)
                k = k + 6
        DoseData.append(InfoList)
    
    def Split(lst):
        return (lst[0].split())


    def SearchDose(DoseNumber,DoseType):
        Count =  0
        List = []
        for i in range(0,len(HospitalName45)) :
            flag = 0
            Info = []
            for j in range(0,len(DoseData[i])) :
                if DoseData[i][j].Status == "Available" :
                    if DoseData[i][j].Vaccine == DoseType :
                        if DoseNumber == 1 :
                            if DoseData[i][j].Dose1 != "-1" and DoseData[i][j].Dose1.replace(" ","") != "0" :
                                flag = 1 
                                date = str(datetime.today() + timedelta(j))
                                Info.append(DoseSearch(date[0:10],DoseData[i][j].Dose1))
                                # ##print(j)
                        elif DoseNumber == 2 :
                            if DoseData[i][j].Dose2 != "-1" and DoseData[i][j].Dose2.replace(" ","") != "0":
                                flag = 1 
                                date = str(datetime.today() + timedelta(j))
                                Info.append(DoseSearch(date[0:10],DoseData[i][j].Dose2))
                                # ##print(HospitalName45[i])
            if flag == 1 :
                Count = Count + 1 
                List.append(SearchTemplate(HospitalName45[i],Address45[i],Info))
        return SearchResult(Count,List)



    ReturnStatement = ""
    RS = []
    VaccType = ""
    if VaccineType == "1" :
        VaccType = "COVISHIELD"
    elif VaccineType == "2" :
        VaccType = "COVAXIN"
    if AgeChoice == "1" :
        SR = SearchDose18(int(VaccineDose),VaccType)
    elif AgeChoice == "2" :
        SR = SearchDose(int(VaccineDose),VaccType)
    if SR.NoOfSlots == 0 :
        ReturnStatement = "No Slots Available"
        RS.append(ReturnStatement)
        return RS
    else :
        for j in range(0,len(SR.SlotInfo)) :
            ReturnStatement = ReturnStatement + ("\n\nHospital Name : " + SR.SlotInfo[j].HospitalName + "\nHospital Address : " + SR.SlotInfo[j].HospitalAdress) + "\n"
            for k in range(0,len(SR.SlotInfo[j].Dose)) :
                ReturnStatement = ReturnStatement + ("Date : " + SR.SlotInfo[j].Dose[k].Date + "   No of Slots : " +  f'{SR.SlotInfo[j].Dose[k].NoOfSlots}' + "\n")
            RS.append(ReturnStatement)
            ReturnStatement = ""

    driver.quit()
    return RS