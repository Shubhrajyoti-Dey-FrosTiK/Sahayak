def InfoState(state) :
    # StateInfoDictionary = {
    #     "AndamanAndNicobarIslands" : "0",
    #     "AndhraPradesh" : "1",
    #     "ArunachalPradesh" : "2",
    #     "Assam" : "3",
    #     "Bihar" : "4",
    #     "Chandigarh" : "5",
    #     "Chhattisgarh" : "6",
    #     "DadraAndNagarHaveli" : "7",
    #     "DamanAndDiu" : "8",
    #     "Delhi" : "9",
    #     "Goa" : "10",
    #     "Gujarat" : "11",
    #     "Haryana" : "12",
    #     "HimachalPradesh" : "13",
    #     "JammuAndKashmir" : "14",
    #     "Jharkhand" : "15",
    #     "Karnataka" : "16",
    #     "Kerala" : "17",
    #     "Ladakh" : "18",
    #     "Lakshadweep" : "19",
    #     "MadhyaPradesh" : "20",
    #     "Maharashtra" : "21",
    #     "Manipur" : "22",
    #     "Meghalaya" : "23",
    #     "Mizoram" : "24",
    #     "Nagaland" : "25",
    #     "Odisha" : "26",
    #     "Puducherry" : "27",
    #     "Punjab" : "28",
    #     "Rajasthan" : "29",
    #     "Sikkim" : "30",
    #     "TamilNadu" : "31",
    #     "Telangana" : "32",
    #     "Tripura" : "33",
    #     "UttarPradesh" : "34",
    #     "Uttarakhand" : "35",
    #     "WestBengal" : "36",
    # }

    StateInfoDictionary = {
        "ANDAMANANDNICOBARISLANDS" : "0",
        "ANDHRAPRADESH" : "1",
        "ARUNACHALPRADESH" : "2",
        "ASSAM" : "3",
        "BIHAR" : "4",
        "CHANDIGARH" : "5",
        "CHHATTISGARH" : "6",
        "DADRAANDNAGARHAVELI" : "7",
        "DAMANANDDIU" : "8",
        "DELHI" : "9",
        "GOA" : "10",
        "GUJARAT" : "11",
        "HARYANA" : "12",
        "HIMACHALPRADESH" : "13",
        "JAMMUANDKASHMIR" : "14",
        "JHARKHAND" : "15",
        "KARNATAKA" : "16",
        "KERALA" : "17",
        "LADAKH" : "18",
        "LAKSHADWEEP" : "19",
        "MADHYAPRADESH" : "20",
        "MAHARASHTRA" : "21",
        "MANIPUR" : "22",
        "MEGHALAYA" : "23",
        "MIZORAM" : "24",
        "NAGALAND" : "25",
        "ODISHA" : "26",
        "PUDUCHERRY" : "27",
        "PUNJAB" : "28",
        "RAJASTHAN" : "29",
        "SIKKIM" : "30",
        "TAMILNADU" : "31",
        "TELANGANA" : "32",
        "TRIPURA" : "33",
        "UTTARPRADESH" : "34",
        "UTTARAKHAND" : "35",
        "WESTBENGAL" : "36",
    }

    try:
        s=StateInfoDictionary[state]
        return s
    except KeyError as ke:
        return "-1"

def InfoCity(city) :
    CityInfoDictionary = {
        # Andaman and Nicobar 
        "Nicobar" : "270",
        "North And Middle Andaman" : "271",
        "South Andaman" : "272",
        
        # Andhra Pradesh 
        "Anantapur" : "273",
        "Chittoor" : "274",
        "East Godavari" : "275",
        "Guntur" : "276",
        "Krishna" : "277",
        "Kurnool" : "278",
        "Prakasam" : "279",
        "Sri Potti Sriramulu Nellore" : "280",
        "Srikakulam" : "281",
        "Visakhapatnam" : "282",
        "Vizianagaram" : "283",
        "West Godavari" : "284",
        "YSR District, Kadapa (Cuddapah)" : "285",

        #Arunachal Pradesh
        "Anjaw" : "286",
        "Changlang" : "287",
        "Dibang Valley" : "288",
        "East Kameng" : "289",
        "East Siang" : "290",
        "Itanagar Capital Complex" : "291",
        "Kamle" : "292",
        "Kra Daadi" : "293",
        "Kurung Kumey" : "294",
        "Lepa Rada" : "295",
        "Lohit" : "296",
        "Longding" : "297",
        "Lower Dibang Valley" : "298",
        "Lower Siang" : "299",
        "Lower Subansiri" : "300",
        "Namsai" : "301",
        "Pakke Kessang" : "302",
        "Papum Pare" : "303",
        "Shi Yomi" : "304",
        "Siang" : "305",
        "Tawang" : "306",
        "Tirap" : "307",
        "Upper Siang" : "308",
        "Upper Subansiri" : "309",
        "West Kameng" : "310",
        "West Siang" : "311",

        # Assam 
        "Baksa" : "312",
        "Barpeta" : "313",
        "Biswanath" : "314",
        "Bongaigaon" : "315",
        "Cachar" : "316",
        "Charaideo" : "317",
        "Chirang" : "318",
        "Darrang" : "319",
        "Dhemaji" : "320",
        "Dhubri" : "321",
        "Dibrugarh" : "322",
        "Dima Hasao" : "323",
        "Goalpara" : "324",
        "Golaghat" : "325",
        "Hailakandi" : "326",
        "Hojai" : "327",
        "Jorhat" : "328",
        "Kamrup Metropolitan" : "329",
        "Kamrup Rural" : "330",
        "Karbi-Anglong" : "331",
        "Karimganj" : "332",
        "Kokrajhar" : "333",
        "Lakhimpur" : "334",
        "Majuli" : "335",
        "Morigaon" : "336",
        "Nagaon" : "337",
        "Nalbari" : "338",
        "Sivasagar" : "339",
        "Sonitpur" : "340",
        "South Salmara Mankachar" : "341",
        "Tinsukia" : "342",
        "Udalguri" : "343",
        "West Karbi Anglong" : "344",

        # Bihar 
        "Araria" : "345",
        "Arwal" : "346",
        "Aurangabad" : "347",
        "Banka" : "348",
        "Begusarai" : "349",
        "Bhagalpur" : "350",
        "Bhojpur" : "351",
        "Buxar" : "352",
        "Darbhanga" : "353",
        "East Champaran" : "354",
        "Gaya" : "355",
        "Gopalganj" : "356",
        "Jamui" : "357",
        "Jehanabad" : "358",
        "Kaimur" : "359",
        "Katihar" : "360",
        "Khagaria" : "361",
        "Kishanganj" : "362",
        "Lakhisarai" : "363",
        "Madhepura" : "364",
        "Madhubani" : "365",
        "Munger" : "366",
        "Muzaffarpur" : "367",
        "Nalanda" : "368",
        "Nawada" : "369",
        "Patna" : "370",
        "Purnia" : "371",
        "Rohtas" : "372",
        "Saharsa" : "373",
        "Samastipur" : "374",
        "Saran" : "375",
        "Sheikhpura" : "376",
        "Sheohar" : "377",
        "Sitamarhi" : "378",
        "Siwan" : "379",
        "Supaul" : "380",
        "Vaishali" : "381",
        "West Champaran" : "382",

        # Chandigarh 
        "Chandigarh" : "383",

        # Chattisgrah 
        "Balod" : "384",
        "Baloda Bazar" : "385",
        "Balrampur" : "386",
        "Bastar" : "387",
        "Bemetara" : "388",
        "Bijapur" : "389",
        "Bilaspur" : "390",
        "Dantewada" : "391",
        "Dhamtari" : "392",
        "Durg" : "393",
        "Gariaband" : "394",
        "Gaurela Pendra Marwahi" : "395",
        "Janjgir-Champa" : "396",
        "Jashpur" : "397",
        "Kanker" : "398",
        "Kawardha" : "399",
        "Kondagaon" : "400",
        "Korba" : "401",
        "Koriya" : "402",
        "Mahasamund" : "403",
        "Mungeli" : "404",
        "Narayanpur" : "405",
        "Raigarh" : "406",
        "Raipur" : "407",
        "Rajnandgaon" : "408",
        "Sukma" : "409",
        "Surajpur" : "410",
        "Surguja" : "411",

        # Dadra and Nagae Haveli 
        "Dadra And Nagar Haveli" : "412",

        # Daman and Diu 
        "Daman" : "413",
        "Diu" : "414",

        # Delhi 
        "Central Delhi" : "415",
        "East Delhi" : "416",
        "New Delhi" : "417",
        "North Delhi" : "418",
        "North East Delhi" : "419",
        "North West Delhi" : "420",
        "Shahdara" : "421",
        "South Delhi" : "422",
        "South East Delhi" : "423",
        "South West Delhi" : "424",
        "West Delhi" : "425",

        #Goa
        "North Goa" : "426",
        "South Goa" : "427",

        # Gujarat 
        "Ahmedabad" : "583",
        "Ahmedabad Corporation" : "584",
        "Amreli" : "585",
        "Anand" : "586",
        "Aravalli" : "587",
        "Banaskantha" : "588",
        "Bharuch" : "589",
        "Bhavnagar" : "590",
        "Bhavnagar Corporation" : "591",
        "Botad" : "592",
        "Chhotaudepur" : "593",
        "Dahod" : "594",
        "Dang" : "595",
        "Devbhumi Dwaraka" : "596",
        "Gandhinagar" : "597",
        "Gandhinagar Corporation" : "598",
        "Gir Somnath" : "599",
        "Jamnagar" : "600",
        "Jamnagar Corporation" : "601",
        "Junagadh" : "602",
        "Junagadh Corporation" : "603",
        "Kheda" : "604",
        "Kutch" : "605",
        "Mahisagar" : "606",
        "Mehsana" : "607",
        "Morbi" : "608",
        "Narmada" : "609",
        "Navsari" : "610",
        "Panchmahal" : "611",
        "Patan" : "612",
        "Porbandar" : "613",
        "Rajkot" : "614",
        "Rajkot Corporation" : "615",
        "Sabarkantha" : "616",
        "Surat" : "617",
        "Surat Corporation" : "618",
        "Surendranagar" : "619",
        "Tapi" : "620",
        "Vadodara" : "621",
        "Vadodara Corporation" : "622",
        "Valsad" : "623",

        # Haryana 
        "Ambala" : "624",
        "Bhiwani" : "625",
        "Charkhi Dadri" : "626",
        "Faridabad" : "627",
        "Fatehabad" : "628",
        "Gurgaon" : "629",
        "Hisar" : "630",
        "Jhajjar" : "631",
        "Jind" : "632",
        "Kaithal" : "633",
        "Karnal" : "634",
        "Kurukshetra" : "635",
        "Mahendragarh" : "636",
        "Nuh" : "637",
        "Palwal" : "638",
        "Panchkula" : "639",
        "Panipat" : "640",
        "Rewari" : "641",
        "Rohtak" : "642",
        "Sirsa" : "643",
        "Sonipat" : "644",
        "Yamunanagar" : "645",

        # Himachal Pradesh 
        "Bilaspur" : "646",
        "Chamba" : "647",
        "Hamirpur" : "648",
        "Kangra" : "649",
        "Kinnaur" : "650",
        "Kullu" : "651",
        "Lahaul Spiti" : "652",
        "Mandi" : "653",
        "Shimla" : "654",
        "Sirmaur" : "655",
        "Solan" : "656",
        "Una" : "657",

        # Jammu and Kashmir 
        "Anantnag" : "658",
        "Bandipore" : "659",
        "Baramulla" : "660",
        "Budgam" : "661",
        "Doda" : "662",
        "Ganderbal" : "663",
        "Jammu" : "664",
        "Kathua" : "665",
        "Kishtwar" : "666",
        "Kulgam" : "667",
        "Kupwara" : "668",
        "Poonch" : "669",
        "Pulwama" : "670",
        "Rajouri" : "671",
        "Ramban" : "672",
        "Reasi" : "673",
        "Samba" : "674",
        "Shopian" : "675",
        "Srinagar" : "676",
        "Udhampur" : "677",

        # Jharkhand 
        "Bokaro" : "678",
        "Chatra" : "679",
        "Deoghar" : "680",
        "Dhanbad" : "681",
        "Dumka" : "682",
        "East Singhbhum" : "683",
        "Garhwa" : "684",
        "Giridih" : "685",
        "Godda" : "686",
        "Gumla" : "687",
        "Hazaribagh" : "688",
        "Jamtara" : "689",
        "Khunti" : "690",
        "Koderma" : "691",
        "Latehar" : "692",
        "Lohardaga" : "693",
        "Pakur" : "694",
        "Palamu" : "695",
        "Ramgarh" : "696",
        "Ranchi" : "697",
        "Sahebganj" : "698",
        "Seraikela Kharsawan" : "699",
        "Simdega" : "700",
        "West Singhbhum" : "701",

        # Karnataka 
        "Bagalkot" : "702",
        "Bangalore Rural" : "703",
        "Bangalore Urban" : "704",
        "BBMP" : "705",
        "Belgaum" : "706",
        "Bellary" : "707",
        "Bidar" : "708",
        "Chamarajanagar" : "709",
        "Chikamagalur" : "710",
        "Chikkaballapur" : "711",
        "Chitradurga" : "712",
        "Dakshina Kannada" : "713",
        "Davanagere" : "714",
        "Dharwad" : "715",
        "Gadag" : "716",
        "Gulbarga" : "717",
        "Hassan" : "718",
        "Haveri" : "719",
        "Kodagu" : "720",
        "Kolar" : "721",
        "Koppal" : "722",
        "Mandya" : "723",
        "Mysore" : "724",
        "Raichur" : "725",
        "Ramanagara" : "726",
        "Shimoga" : "727",
        "Tumkur" : "728",
        "Udupi" : "729",
        "Uttar Kannada" : "730",
        "Vijayapura" : "731",
        "Yadgir" : "732",

        # Kerela 
        "Alappuzha" : "733",
        "Ernakulam" : "734",
        "Idukki" : "735",
        "Kannur" : "736",
        "Kasaragod" : "737",
        "Kollam" : "738",
        "Kottayam" : "739",
        "Kozhikode" : "740",
        "Malappuram" : "741",
        "Palakkad" : "742",
        "Pathanamthitta" : "743",
        "Thiruvananthapuram" : "744",
        "Thrissur" : "745",
        "Wayanad" : "746",

        # Ladakh 
        "Kargil" : "747",
        "Leh" : "748",

        # Lakshadweep 
        "Agatti Island" : "749",
        "Lakshadweep" : "750",

        # Madhya Pradesh 
        "Agar" : "751",
        "Alirajpur" : "752",
        "Anuppur" : "753",
        "Ashoknagar" : "754",
        "Balaghat" : "755",
        "Barwani" : "756",
        "Betul" : "757",
        "Bhind" : "758",
        "Bhopal" : "759",
        "Burhanpur" : "760",
        "Chhatarpur" : "761",
        "Chhindwara" : "762",
        "Damoh" : "763",
        "Datia" : "764",
        "Dewas" : "765",
        "Dhar" : "766",
        "Dindori" : "767",
        "Guna" : "768",
        "Gwalior" : "769",
        "Harda" : "770",
        "Hoshangabad" : "771",
        "Indore" : "772",
        "Jabalpur" : "773",
        "Jhabua" : "774",
        "Katni" : "775",
        "Khandwa" : "776",
        "Khargone" : "777",
        "Mandla" : "778",
        "Mandsaur" : "779",
        "Morena" : "780",
        "Narsinghpur" : "781",
        "Neemuch" : "782",
        "Panna" : "783",
        "Raisen" : "784",
        "Rajgarh" : "785",
        "Ratlam" : "786",
        "Rewa" : "787",
        "Sagar" : "788",
        "Satna" : "789",
        "Sehore" : "790",
        "Seoni" : "791",
        "Shahdol" : "792",
        "Shajapur" : "793",
        "Sheopur" : "794",
        "Shivpuri" : "795",
        "Sidhi" : "796",
        "Singrauli" : "797",
        "Tikamgarh" : "798",
        "Ujjain" : "799",
        "Umaria" : "800",
        "Vidisha" : "801",

        # Maharashtra 
        "Ahmednagar" : "802",
        "Akola" : "803",
        "Amravati" : "804",
        "Aurangabad" : "805",
        "Beed" : "806",
        "Bhandara" : "807",
        "Buldhana" : "808",
        "Chandrapur" : "809",
        "Dhule" : "810",
        "Gadchiroli" : "811",
        "Gondia" : "812",
        "Hingoli" : "813",
        "Jalgaon" : "814",
        "Jalna" : "815",
        "Kolhapur" : "816",
        "Latur" : "817",
        "Mumbai" : "818",
        "Nagpur" : "819",
        "Nanded" : "820",
        "Nandurbar" : "821",
        "Nashik" : "822",
        "Osmanabad" : "823",
        "Palghar" : "824",
        "Parbhani" : "825",
        "Pune" : "826",
        "Raigad" : "827",
        "Ratnagiri" : "828",
        "Sangli" : "829",
        "Satara" : "830",
        "Sindhudurg" : "831",
        "Solapur" : "832",
        "Thane" : "833",
        "Wardha" : "834",
        "Washim" : "835",
        "Yavatmal" : "836",

        # Manipur 
        "Bishnupur" : "837",
        "Chandel" : "838",
        "Churachandpur" : "839",
        "Imphal East" : "840",
        "Imphal West" : "841",
        "Jiribam" : "842",
        "Kakching" : "843",
        "Kamjong" : "844",
        "Kangpokpi" : "845",
        "Noney" : "846",
        "Pherzawl" : "847",
        "Senapati" : "848",
        "Tamenglong" : "849",
        "Tengnoupal" : "850",
        "Thoubal" : "851",
        "Ukhrul" : "852",

        # Meghalaya 
        "East Garo Hills" : "853",
        "East Jaintia Hills" : "854",
        "East Khasi Hills" : "855",
        "North Garo Hills" : "856",
        "Ri-Bhoi" : "857",
        "South Garo Hills" : "858",
        "South West Garo Hills" : "859",
        "South West Khasi Hills" : "860",
        "West Garo Hills" : "861",
        "West Jaintia Hills" : "862",
        "West Khasi Hills" : "863",

        # Mizoram 
        "Aizawl East" : "864",
        "Aizawl West" : "865",
        "Champhai" : "866",
        "Kolasib" : "867",
        "Lawngtlai" : "868",
        "Lunglei" : "869",
        "Mamit" : "870",
        "Serchhip" : "871",
        "Siaha" : "872",

        # Nagaland
        "Dimapur" : "873",
        "Kiphire" : "874",
        "Kohima" : "875",
        "Longleng" : "876",
        "Mokokchung" : "877",
        "Mon" : "878",
        "Peren" : "879",
        "Phek" : "880",
        "Tuensang" : "881",
        "Wokha" : "882",
        "Zunheboto" : "883",

        # Odisha 
        "Angul" : "884",
        "Balangir" : "885",
        "Balasore" : "886",
        "Bargarh" : "887",
        "Bhadrak" : "888",
        "Boudh" : "889",
        "Cuttack" : "890",
        "Deogarh" : "891",
        "Dhenkanal" : "892",
        "Gajapati" : "893",
        "Ganjam" : "894",
        "Jagatsinghpur" : "895",
        "Jajpur" : "896",
        "Jharsuguda" : "897",
        "Kalahandi" : "898",
        "Kandhamal" : "899",
        "Kendrapara" : "900",
        "Kendujhar" : "901",
        "Khurda" : "902",
        "Koraput" : "903",
        "Malkangiri" : "904",
        "Mayurbhanj" : "905",
        "Nabarangpur" : "906",
        "Nayagarh" : "907",
        "Nuapada" : "908",
        "Puri" : "909",
        "Rayagada" : "910",
        "Sambalpur" : "911",
        "Subarnapur" : "912",
        "Sundargarh" : "913",

        # Puducherrey 
        "Karaikal" : "914",
        "Mahe" : "915",
        "Puducherry" : "916",
        "Yanam" : "917",

        # Punjab 
        "Amritsar" : "918",
        "Barnala" : "919",
        "Bathinda" : "920",
        "Faridkot" : "921",
        "Fatehgarh Sahib" : "922",
        "Fazilka" : "923",
        "Ferozpur" : "924",
        "Gurdaspur" : "925",
        "Hoshiarpur" : "926",
        "Jalandhar" : "927",
        "Kapurthala" : "928",
        "Ludhiana" : "929",
        "Mansa" : "930",
        "Moga" : "931",
        "Pathankot" : "932",
        "Patiala" : "933",
        "Rup Nagar" : "934",
        "Sangrur" : "935",
        "SAS Nagar" : "936",
        "SBS Nagar" : "937",
        "Sri Muktsar Sahib" : "938",
        "Tarn Taran" : "939",

        # Rajasthan 
        "Ajmer" : "940",
        "Alwar" : "941",
        "Banswara" : "942",
        "Baran" : "943",
        "Barmer" : "944",
        "Bharatpur" : "945",
        "Bhilwara" : "946",
        "Bikaner" : "947",
        "Bundi" : "948",
        "Chittorgarh" : "949",
        "Churu" : "950",
        "Dausa" : "951",
        "Dholpur" : "952",
        "Dungarpur" : "953",
        "Hanumangarh" : "954",
        "Jaipur I" : "955",
        "Jaipur II" : "956",
        "Jaisalmer" : "957",
        "Jalore" : "958",
        "Jhalawar" : "959",
        "Jhunjhunu" : "960",
        "Jodhpur" : "961",
        "Karauli" : "962",
        "Kota" : "963",
        "Nagaur" : "964",
        "Pali" : "965",
        "Pratapgarh" : "966",
        "Rajsamand" : "967",
        "Sawai Madhopur" : "968",
        "Sikar" : "969",
        "Sirohi" : "970",
        "Sri Ganganagar" : "971",
        "Tonk" : "972",
        "Udaipur" : "973",
        
        # Sikkim
        "East Sikkim" : "974",
        "North Sikkim" : "975",
        "South Sikkim" : "976",
        "West Sikkim" : "977",

        # Tamil Nadu 
        "Aranthangi" : "978",
        "Ariyalur" : "979",
        "Attur" : "980",
        "Chengalpet" : "981",
        "Chennai" : "982",
        "Cheyyar" : "983",
        "Coimbatore" : "984",
        "Cuddalore" : "985",
        "Dharmapuri" : "986",
        "Dindigul" : "987",
        "Erode" : "988",
        "Kallakurichi" : "989",
        "Kanchipuram" : "990",
        "Kanyakumari" : "991",
        "Karur" : "992",
        "Kovilpatti" : "993",
        "Krishnagiri" : "994",
        "Madurai" : "995",
        "Nagapattinam" : "996",
        "Namakkal" : "997",
        "Nilgiris" : "998",
        "Palani" : "999",
        "Paramakudi" : "1000",
        "Perambalur" : "1001",
        "Poonamallee" : "1002",
        "Pudukkottai" : "1003",
        "Ramanathapuram" : "1004",
        "Ranipet" : "1005",
        "Salem" : "1006",
        "Sivaganga" : "1007",
        "Sivakasi" : "1008",
        "Tenkasi" : "1009",
        "Thanjavur" : "1010",
        "Theni" : "1011",
        "Thoothukudi (Tuticorin)" : "1012",
        "Tiruchirappalli" : "1013",
        "Tirunelveli" : "1014",
        "Tirupattur" : "1015",
        "Tiruppur" : "1016",
        "Tiruvallur" : "1017",
        "Tiruvannamalai" : "1018",
        "Tiruvarur" : "1019",
        "Vellore" : "1020",
        "Viluppuram" : "1021",
        "Virudhunagar" : "1022",

        # Telengana
        "Adilabad" : "1023",
        "Bhadradri Kothagudem" : "1024",
        "Hyderabad" : "1025",
        "Jagtial" : "1026",
        "Jangaon" : "1027",
        "Jayashankar Bhupalpally" : "1028",
        "Jogulamba Gadwal" : "1029",
        "Kamareddy" : "1030",
        "Karimnagar" : "1031",
        "Khammam" : "1032",
        "Kumuram Bheem" : "1033",
        "Mahabubabad" : "1034",
        "Mahabubnagar" : "1035",
        "Mancherial" : "1036",
        "Medak" : "1037",
        "Medchal" : "1038",
        "Mulugu" : "1039",
        "Nagarkurnool" : "1040",
        "Nalgonda" : "1041",
        "Narayanpet" : "1042",
        "Nirmal" : "1043",
        "Nizamabad" : "1044",
        "Peddapalli" : "1045",
        "Rajanna Sircilla" : "1046",
        "Rangareddy" : "1047",
        "Sangareddy" : "1048",
        "Siddipet" : "1049",
        "Suryapet" : "1050",
        "Vikarabad" : "1051",
        "Wanaparthy" : "1052",
        "Warangal(Rural)" : "1053",
        "Warangal(Urban)" : "1054",
        "Yadadri Bhuvanagiri" : "1055",

        # Tripura
        "Dhalai" : "1056",
        "Gomati" : "1057",
        "Khowai" : "1058",
        "North Tripura" : "1059",
        "Sepahijala" : "1060",
        "South Tripura" : "1061",
        "Unakoti" : "1062",
        "West Tripura" : "1063",

        # Uttar Pradesh 
        "Agra" : "1064",
        "Aligarh" : "1065",
        "Ambedkar Nagar" : "1066",
        "Amethi" : "1067",
        "Amroha" : "1068",
        "Auraiya" : "1069",
        "Ayodhya" : "1070",
        "Azamgarh" : "1071",
        "Badaun" : "1072",
        "Baghpat" : "1073",
        "Bahraich" : "1074",
        "Balarampur" : "1075",
        "Ballia" : "1076",
        "Banda" : "1077",
        "Barabanki" : "1078",
        "Bareilly" : "1079",
        "Basti" : "1080",
        "Bhadohi" : "1081",
        "Bijnour" : "1082",
        "Bulandshahr" : "1083",
        "Chandauli" : "1084",
        "Chitrakoot" : "1085",
        "Deoria" : "1086",
        "Etah" : "1087",
        "Etawah" : "1088",
        "Farrukhabad" : "1089",
        "Fatehpur" : "1090",
        "Firozabad" : "1091",
        "Gautam Buddha Nagar" : "1092",
        "Ghaziabad" : "1093",
        "Ghazipur" : "1094",
        "Gonda" : "1095",
        "Gorakhpur" : "1096",
        "Hamirpur" : "1097",
        "Hapur" : "1098",
        "Hardoi" : "1099",
        "Hathras" : "1100",
        "Jalaun" : "1101",
        "Jaunpur" : "1102",
        "Jhansi" : "1103",
        "Kannauj" : "1104",
        "Kanpur Dehat" : "1105",
        "Kanpur Nagar" : "1106",
        "Kasganj" : "1107",
        "Kaushambi" : "1108",
        "Kushinagar" : "1109",
        "Lakhimpur Kheri" : "1110",
        "Lalitpur" : "1111",
        "Lucknow" : "1112",
        "Maharajganj" : "1113",
        "Mahoba" : "1114",
        "Mainpuri" : "1115",
        "Mathura" : "1116",
        "Mau" : "1117",
        "Meerut" : "1118",
        "Mirzapur" : "1119",
        "Moradabad" : "1120",
        "Muzaffarnagar" : "1121",
        "Pilibhit" : "1122",
        "Pratapgarh" : "1123",
        "Prayagraj" : "1124",
        "Raebareli" : "1125",
        "Rampur" : "1126",
        "Saharanpur" : "1127",
        "Sambhal" : "1128",
        "Sant Kabir Nagar" : "1129",
        "Shahjahanpur" : "1130",
        "Shamli" : "1131",
        "Shravasti" : "1132",
        "Siddharthnagar" : "1133",
        "Sitapur" : "1134",
        "Sonbhadra" : "1135",
        "Sultanpur" : "1136",
        "Unnao" : "1137",
        "Varanasi" : "1138",

        # Uttarakhand
        "Almora" : "1139",
        "Bageshwar" : "1140",
        "Chamoli" : "1141",
        "Champawat" : "1142",
        "Dehradun" : "1143",
        "Haridwar" : "1144",
        "Nainital" : "1145",
        "Pauri Garhwal" : "1146",
        "Pithoragarh" : "1147",
        "Rudraprayag" : "1148",
        "Tehri Garhwal" : "1149",
        "Udham Singh Nagar" : "1150",
        "Uttarkashi" : "1151",
        
        # West Bengal 
        "Alipurduar District" : "1152",
        "Bankura" : "1153",
        "Basirhat HD (North 24 Parganas)" : "1154",
        "Birbhum" : "1155",
        "Bishnupur HD (Bankura)" : "1156",
        "Cooch Behar" : "1157",
        "COOCHBEHAR" : "1158",
        "Dakshin Dinajpur" : "1159",
        "Darjeeling" : "1160",
        "Diamond Harbor HD (S 24 Parganas)" : "1161",
        "East Bardhaman" : "1162",
        "Hoogly" : "1163",
        "Howrah" : "1164",
        "Jalpaiguri" : "1165",
        "Jhargram" : "1166",
        "Kalimpong" : "1167",
        "Kolkata" : "1168",
        "Malda" : "1169",
        "Murshidabad" : "1170",
        "Nadia" : "1171",
        "Nandigram HD (East Medinipore)" : "1172",
        "North 24 Parganas" : "1173",
        "Paschim Medinipore" : "1174",
        "Purba Medinipore" : "1175",
        "Purulia" : "1176",
        "Rampurhat HD (Birbhum)" : "1177",
        "South 24 Parganas" : "1178",
        "Uttar Dinajpur" : "1179",
        "West Bardhaman" : "1180",

    }
    try:
        s=CityInfoDictionary[city]
        return s
    except KeyError as ke:
        return "-1"