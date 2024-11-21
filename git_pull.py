import requests
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
complete_detail = response.json()
for i in range (len(complete_detail)):
    print(complete_detail[i]["user"]["login"])




### Get pull request information on reporting in python 
kubernets-user_name
kubernetes-repo_name

1-first insatll request pip install request
2- go to Google type github api after copy path pull request
3-dictonary
4- print 
