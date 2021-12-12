# This calculates Cost of Base Cup without any pkgs, printing, freight.
# It takes requied data from RawMaterialDataSet
# & inputs from user (inputs like: Size, NewGSM, PaperRate, ScrapeRate, Margin)
# output is a number which is Cost of 1 Cup in three desimials .


import json


with open("calculator/utils/calibrate_data/base_cup_data.json") as f:
    RM_Data = json.load(f)


def BaseCupCost(
    Dcs, NoB, WBperS, BW, Overhead, C_Gsm, N_Gsm, PaperRate, ScrapeRate, Margin
):
    N_Dcs = Dcs * N_Gsm / C_Gsm
    N_WBperS = WBperS * N_Gsm / C_Gsm
    OneCup = N_WBperS / NoB
    AddScrap = (N_Dcs - N_WBperS) / NoB
    BottomScrap = BW * 0.4
    TotalPaperperCupIncWaste = (OneCup + AddScrap + BottomScrap + BW) * 1.03
    ScrapGen = AddScrap + BottomScrap  # + (OneCup + AddScrap + BottomScrap + BW) * 0.03
    TotalPaperCostIncOverhead = TotalPaperperCupIncWaste * PaperRate / 1000 + Overhead
    MarginValue = TotalPaperCostIncOverhead * Margin * 0.01
    NewCost = TotalPaperCostIncOverhead + MarginValue
    RecfromScrape = ScrapGen * ScrapeRate / 1000
    FinalPrice = NewCost - RecfromScrape

    return round(FinalPrice, 3)


def base_cup_cost_calculator(size_of_cup, gsm, paper_rate, scrape_rate, margin):

    return BaseCupCost(
        Dcs=RM_Data[size_of_cup]["Die Cup Sheet"],
        NoB=RM_Data[size_of_cup]["Number of Blanks per Sheet"],
        WBperS=RM_Data[size_of_cup]["Wt. Blanks per Sheet"],
        BW=RM_Data[size_of_cup]["Bottom"],
        Overhead=RM_Data[size_of_cup]["Over heads"],
        C_Gsm=RM_Data[size_of_cup]["GSM"],
        N_Gsm=gsm,
        PaperRate=paper_rate,
        ScrapeRate=scrape_rate,
        Margin=margin,
    )
