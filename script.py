import requests
import re
import json

def process_request(endpoint,r_data):  
    r=requests.post(url=endpoint,data=r_data)  
    response_text=r.json()["result"]
    out_list=re.findall('(?<=\d">)(.*?)<',response_text)
    return(out_list)

def get_districts(state):    # get districts in a state
    endpoint_= "https://voterlist.election.gov.np/bbvrs1/index_process_1.php"

    r_data={"state":str(state),"list_type":"district"}

    headers={
        "Host": "voterlist.election.gov.np",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:114.0) Gecko/20100101 Firefox/114.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Length": "26",
        "Origin": "https://voterlist.election.gov.np",
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": "https://voterlist.election.gov.np/bbvrs1/index_2.php",
        "Cookie": "PHPSESSID=sodu0p5r34m1fve5hm3r6sl0o0",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
    }

    r=process_request(endpoint_,r_data)
    return(r)

def get_vdcs(district):

    r_data={"district":str(district),"list_type":"vdc"}

    endpoint_= "https://voterlist.election.gov.np/bbvrs1/index_process_1.php"

    headers={
        "Host": "voterlist.election.gov.np",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:114.0) Gecko/20100101 Firefox/114.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Length": "25",
        "Origin": "https://voterlist.election.gov.np",
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": "https://voterlist.election.gov.np/bbvrs1/index_2.php",
        "Cookie": "PHPSESSID=sodu0p5r34m1fve5hm3r6sl0o0",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
        }
    
    r=process_request(endpoint_,r_data)
    return(r)

def get_wards(vdc):
    endpoint_= "https://voterlist.election.gov.np/bbvrs1/index_process_1.php"
    
    r_data={"vdc":str(vdc),"list_type":"ward"}
    
    headers={
        "Host": "voterlist.election.gov.np",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:114.0) Gecko/20100101 Firefox/114.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Length": "23",
        "Origin": "https://voterlist.election.gov.np",
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": "https://voterlist.election.gov.np/bbvrs1/index_2.php",
        "Cookie": "PHPSESSID=sodu0p5r34m1fve5hm3r6sl0o0",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
    }

    r=process_request(endpoint_,r_data)
    return(r)

def get_voting_pool(vdc,ward):
    endpoint_= "https://voterlist.election.gov.np/bbvrs1/index_process_1.php"

    r_data={"vdc":str(vdc),"ward":str(ward),"list_type":"reg_centre"}

    headers={
        "Host": "voterlist.election.gov.np",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:114.0) Gecko/20100101 Firefox/114.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Length": "36",
        "Origin": "https://voterlist.election.gov.np",
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": "https://voterlist.election.gov.np/bbvrs1/index_2.php",
        "Cookie": "PHPSESSID=sodu0p5r34m1fve5hm3r6sl0o0",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
    }

    r=process_request(endpoint_,r_data)
    return(r)

def final_request(state,district,vdc,ward,reg_centre):

    r_data={"state":str(state),"district":str(district),"vdc_mun":str(vdc),"ward":str(ward),"reg_centre":str(reg_centre)}

    endpoint= "https://voterlist.election.gov.np/bbvrs1/view_ward_1.php"

    headers={
        "Host": "voterlist.election.gov.np",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:114.0) Gecko/20100101 Firefox/114.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "55",
        "Origin": "https://voterlist.election.gov.np",
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": "https://voterlist.election.gov.np/bbvrs1/index_2.php",
        "Cookie": "PHPSESSID=sodu0p5r34m1fve5hm3r6sl0o0",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "iframe",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1"
    }
    return(process_request(endpoint,r_data))

"""
to get the data we need the appropirate values for 
state,district,vdc,ward,voting_pool

all of which are integers
and there is no particular formula to generate all of them
like you would guess the 
state =1
district =1
vdc =1
ward =1
voting_pool =1 
will be a valid sequence but no! 
"i don't like intuitive things" -- the goverment emploee responsible for this mess

so we need to first get all of these things before we can start getting the actual data

we store them in a nested dictionary type and ultimately write the thing to a file in json:
(state)[1:[
    (district)[4:
        (vdc)[35:
            (ward)[1:
                (pool)[
                    1232,2342,345...
                ]
                ...]
            ...]
        ...]
    ...]
...]
in the above example 1,4,35,1,1232 would be a valid sequence of required info to get the data from voting pool 1232.
"""

district_names={}

for x in range(1,8):
    district_names[str(x)]=get_districts(x)
    
print(json.dumps(district_names,indent=4))

print(district_names)
