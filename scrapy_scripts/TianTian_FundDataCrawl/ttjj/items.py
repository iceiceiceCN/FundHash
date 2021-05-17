# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TtjjItem(scrapy.Item):
    # define the fields for your item here like:
    SHORTNAME = scrapy.Field()
    FCODE = scrapy.Field()
    SHARP1 = scrapy.Field()     #夏普率 1年
    SHARP2 = scrapy.Field()     #夏普率 2年
    STDDEV1 = scrapy.Field()    #波动率 1年
    STDDEV2 = scrapy.Field()    #波动率 2年
    MAXRETRA1 = scrapy.Field()  #最大回撤

    MGRID = scrapy.Field()
    MGRNAME = scrapy.Field()

    GP = scrapy.Field()
    ZQ = scrapy.Field()
    HB = scrapy.Field()
    JZC = scrapy.Field()
    
    Week_up = scrapy.Field()
    Week_avg_up = scrapy.Field()
    Week_hs300_up = scrapy.Field()
    Week_rank = scrapy.Field()
    Week_competitors = scrapy.Field()

    Month_up = scrapy.Field()
    Month_avg_up = scrapy.Field()
    Month_hs300_up = scrapy.Field()
    Month_rank = scrapy.Field()
    Month_competitors = scrapy.Field()

    NowYear_up = scrapy.Field()
    NowYear_avg_up = scrapy.Field()
    NowYear_hs300_up = scrapy.Field()
    NowYear_rank = scrapy.Field()
    NowYear_competitors = scrapy.Field()

    Year_up = scrapy.Field()
    Year_avg_up = scrapy.Field()
    Year_hs300_up = scrapy.Field()
    Year_rank = scrapy.Field()
    Year_competitors = scrapy.Field()
    
    TwoYear_up = scrapy.Field()
    TwoYear_avg_up = scrapy.Field()
    TwoYear_hs300_up = scrapy.Field()
    TwoYear_rank = scrapy.Field()
    TwoYear_competitors = scrapy.Field()

    ThreeYear_up = scrapy.Field()
    ThreeYear_avg_up = scrapy.Field()
    ThreeYear_hs300_up = scrapy.Field()
    ThreeYear_rank = scrapy.Field()
    ThreeYear_competitors = scrapy.Field()

    FiveYear_up = scrapy.Field()
    FiveYear_avg_up = scrapy.Field()
    FiveYear_hs300_up = scrapy.Field()
    FiveYear_rank = scrapy.Field()
    FiveYear_competitors = scrapy.Field()

    fundStocks_GPDM_0 = scrapy.Field()
    fundStocks_GPDM_1 = scrapy.Field()
    fundStocks_GPDM_2 = scrapy.Field()
    fundStocks_GPDM_3 = scrapy.Field()
    fundStocks_GPDM_4 = scrapy.Field()
    fundStocks_GPDM_5 = scrapy.Field()
    fundStocks_GPDM_6 = scrapy.Field()
    fundStocks_GPDM_7 = scrapy.Field()
    fundStocks_GPDM_8 = scrapy.Field()
    fundStocks_GPDM_9 = scrapy.Field()

    fundStocks_GPJC_0 = scrapy.Field()
    fundStocks_GPJC_1 = scrapy.Field()
    fundStocks_GPJC_2 = scrapy.Field()
    fundStocks_GPJC_3 = scrapy.Field()
    fundStocks_GPJC_4 = scrapy.Field()
    fundStocks_GPJC_5 = scrapy.Field()
    fundStocks_GPJC_6 = scrapy.Field()
    fundStocks_GPJC_7 = scrapy.Field()
    fundStocks_GPJC_8 = scrapy.Field()
    fundStocks_GPJC_9 = scrapy.Field()

    fundStocks_JZBL_0 = scrapy.Field()
    fundStocks_JZBL_1 = scrapy.Field()
    fundStocks_JZBL_2 = scrapy.Field()
    fundStocks_JZBL_3 = scrapy.Field()
    fundStocks_JZBL_4 = scrapy.Field()
    fundStocks_JZBL_5 = scrapy.Field()
    fundStocks_JZBL_6 = scrapy.Field()
    fundStocks_JZBL_7 = scrapy.Field()
    fundStocks_JZBL_8 = scrapy.Field()
    fundStocks_JZBL_9 = scrapy.Field()

    fundStocks_PCTNVCHG_0 = scrapy.Field()
    fundStocks_PCTNVCHG_1 = scrapy.Field()
    fundStocks_PCTNVCHG_2 = scrapy.Field()
    fundStocks_PCTNVCHG_3 = scrapy.Field()
    fundStocks_PCTNVCHG_4 = scrapy.Field()
    fundStocks_PCTNVCHG_5 = scrapy.Field()
    fundStocks_PCTNVCHG_6 = scrapy.Field()
    fundStocks_PCTNVCHG_7 = scrapy.Field()
    fundStocks_PCTNVCHG_8 = scrapy.Field()
    fundStocks_PCTNVCHG_9 = scrapy.Field()
    
