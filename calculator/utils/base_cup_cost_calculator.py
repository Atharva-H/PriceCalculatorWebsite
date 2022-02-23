# This calculates Cost of Base Cup without any pkgs, printing, freight.
# It takes requied data from RawMaterialDataSet
# & inputs from user (inputs like: Size, NewGSM, PaperRate, ScrapeRate, Margin)
# output is a number which is Cost of 1 Cup in three desimials .


from calculator.models import ProductDim, ProductCalculationData


def BaseCupCost(
    Dcs, NoB, WBperS, BW, Overhead, C_Gsm, N_Gsm, PaperRate, ScrapeRate, Margin
):
    N_Dcs = Dcs * N_Gsm / C_Gsm
    N_WBperS = WBperS * N_Gsm / C_Gsm
    OneCup = N_WBperS / NoB
    AddScrap = (N_Dcs - N_WBperS) / NoB
    BottomScrap = BW * 0.4
    TotalPaperperCupIncWaste = (OneCup + AddScrap + BottomScrap + BW) * 1.03
    ScrapGen = AddScrap + BottomScrap + (OneCup + AddScrap + BottomScrap + BW) * 0.03
    TotalPaperCostIncOverhead = TotalPaperperCupIncWaste * PaperRate / 1000 + Overhead
    MarginValue = TotalPaperCostIncOverhead * Margin * 0.01
    NewCost = TotalPaperCostIncOverhead + MarginValue
    RecfromScrape = ScrapGen * ScrapeRate / 1000
    FinalPrice = NewCost - RecfromScrape

    # print("N_Dcs-", N_Dcs)
    # print("N_WBperS-", N_WBperS)
    # print("OneCup-", OneCup)
    # print("AddScrap-", AddScrap)
    # print("BottomScrap-", BottomScrap)
    # print("TotalPaperperCupIncWaste-", TotalPaperperCupIncWaste)
    # print("ScrapGen-", ScrapGen)
    # print("TotalPaperCostIncOverhead-", TotalPaperCostIncOverhead)
    # print("MarginValue-", MarginValue)
    # print("NewCost-", NewCost)
    # print("RecfromScrape-", RecfromScrape)
    # print("FinalPrice-", FinalPrice)

    return round(FinalPrice, 3)


def base_cup_cost_calculator(
    size_of_cup,
    gsm,
    paper_rate,
    scrape_rate,
    margin,
    bottom_gsm,
):

    product = ProductDim.objects.get(product_name=size_of_cup)
    product_info = ProductCalculationData.objects.get(product_id=product.id)
    if bottom_gsm == 0:
        return BaseCupCost(
            Dcs=product_info.die_cup_sheet,
            NoB=product_info.num_of_blanks_per_sheet,
            WBperS=product_info.weight_blank_per_sheet,
            BW=product_info.weight_bottom,
            Overhead=product_info.over_head_cost,
            C_Gsm=product_info.gsm,
            N_Gsm=gsm,
            PaperRate=paper_rate,
            ScrapeRate=scrape_rate,
            Margin=margin,
        )
    else:
        bottom_weight = (
            bottom_gsm * product_info.weight_bottom / product_info.bottom_gsm
        )
        return BaseCupCost(
            Dcs=product_info.die_cup_sheet,
            NoB=product_info.num_of_blanks_per_sheet,
            WBperS=product_info.weight_blank_per_sheet,
            BW=bottom_weight,
            Overhead=product_info.over_head_cost,
            C_Gsm=product_info.gsm,
            N_Gsm=gsm,
            PaperRate=paper_rate,
            ScrapeRate=scrape_rate,
            Margin=margin,
        )
