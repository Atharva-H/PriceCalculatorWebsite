import json

with open("calculator/utils/calibrate_data/base_cup_data.json") as f:
    RM_Data = json.load(f)

size = RM_Data.keys()


def calibrate(request_body):
    d = {}
    e = {}
    for j in size:
        for i in [
            "GSM",
            "Die Cup Sheet",
            "Number of Blanks per Sheet",
            "Wt. Blanks per Sheet",
            "Bottom",
            "Over heads",
        ]:
            e[i] = int(request_body[f"{j}{i}"][0])
        d[j] = e.copy()
    return d


# def calibrate_done():
#     data=calibrate()
#     with open('calculator\utils\calibrate_data\data.json', 'w') as fp:
#         json.dump(data,fp)
