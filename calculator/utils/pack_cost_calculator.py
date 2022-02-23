# This will calculate cost of 1 sleeve or 1 SKU or 1 Small Pack conatining specific Papercups.

# INPUTS-
# Cost per cup          ==>> From BaseCupCostCalculator
# Cups per SKU          ==>> From User
# SKU per Master carton ==>> From User
# Cost of Printing color==>> From User
# Label/Marking Cost    ==>> From User
# Poly/SmallBox Cost    ==>> From User
# Master Carton Cost    ==>> From User
# Freight               ==>> From User
# No. Boxs Per Container==>> From BoxPerConatiner
# Dollor Rate $$$       ==>> From User
# Addition Cost Per SKU ==>> From User

# OUTPUTS-
# A number which is Cost of 1 SKU in Dollors $$$ in three desimials.
# A number which is Cost of 1 SKU in Rupees ₹₹₹ three desimials.
from rich import print


def PackCost(
    BaseCostperCup,
    CupsperSKU,
    SKUperMC,
    CostPrintColorperCup,
    LabelCost,
    PolyCost,
    MCCost,
    Freight,
    BoxsPerContainer,
    DollorRate,
    AddCostperSKU,
):
    CostLabelperCup = LabelCost / CupsperSKU
    CostPloyperCup = PolyCost / CupsperSKU
    CostMCperCup = MCCost / (CupsperSKU * SKUperMC)
    CostFreightperCup = Freight / (CupsperSKU * SKUperMC * BoxsPerContainer)
    CostAddperCup = AddCostperSKU / CupsperSKU
    TotalCostperCup = (
        BaseCostperCup
        + CostPrintColorperCup
        + CostPloyperCup
        + CostLabelperCup
        + CostMCperCup
        + CostFreightperCup
        + CostAddperCup
    )
    CostperSKUinINR = TotalCostperCup * CupsperSKU
    CostperSKUinDollor = CostperSKUinINR / DollorRate
    CostperMCinINR = TotalCostperCup * CupsperSKU * SKUperMC
    CostperMCinDollor = CostperMCinINR / DollorRate
    print("CostLabelperCup", CostLabelperCup)
    print("  CostPloyperCup", CostPloyperCup)
    print("  CostMCperCup", CostMCperCup)
    print("  CostFreightperCup", CostFreightperCup)
    print("  CostAddperCup", CostAddperCup)
    print("  TotalCostperCup", TotalCostperCup)

    return (
        round(CostperMCinINR, 3),
        round(CostperMCinDollor, 3),
        round(CostperSKUinINR, 3),
        round(CostperSKUinDollor, 3),
    )


def pack_cost_calculator(
    BaseCostperCup,
    CupsperSKU,
    SKUperMC,
    CostPrintColorperCup,
    LabelCost,
    PolyCost,
    MCCost,
    Freight,
    BoxsPerContainer,
    DollorRate,
    AddCostperSKU,
):

    return PackCost(
        BaseCostperCup=BaseCostperCup,
        CupsperSKU=CupsperSKU,
        SKUperMC=SKUperMC,
        CostPrintColorperCup=CostPrintColorperCup,
        LabelCost=LabelCost,
        PolyCost=PolyCost,
        MCCost=MCCost,
        Freight=Freight,
        BoxsPerContainer=BoxsPerContainer,
        DollorRate=DollorRate,
        AddCostperSKU=AddCostperSKU,
    )
