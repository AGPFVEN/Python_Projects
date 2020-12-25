import sys
import requests
sys.path.append("D:\\python_agpfven\\lib\\site-packages")

session_token = "53616c7465645f5f749681237e075d5eb3859efc3228e8e3cb92384406217bbae2149ef63a1453873b5f1159dee661d1"

def download_input(day_num):
    url = "https://adventofcode.com/2020/day/{}/input".format(day_num)
    cookies = {
        "session": session_token
    }

    print("Downloading day {} from {}".format(day_num, url))
    response = requests.get(url, cookies=cookies)
    if response.status_code == 200:
        return response.text
    else:
        print("Download error. {}\n{}".format(response.status_code, response.text))
        exit()

if __name__ == "__main__":
    import sys
    inputs = download(sys.argv[1])
    filename = "day{}inputs".format(sys.argv[1])
    with open(filename, "w") as file:
        file.write(inputs)


download_input(1)