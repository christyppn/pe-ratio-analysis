// Historical P/E Ratio Analysis Data with Fear & Greed Index
export const peRatioAnalysis = {
  summary: {
    title: "主要市場指數歷史本益比分析報告",
    author: "Manus AI",
    date: "2025年10月",
    description: "本報告對主要全球股票市場指數的歷史本益比進行了深入分析，包括標準普爾500指數、道瓊工業平均指數、納斯達克綜合指數以及恒生指數。同時整合了美國和香港市場的恐懼與貪婪指數，提供更全面的市場情緒分析。"
  },
  
  historicalAverages: {
    "PE_Shiller": 17.90,
    "PE_multpl": 15.50,
    "PE_investorsfriend": 20.10,
    "PE_fullratio": 29.56,
    "PE_HSI": 11.83
  },
  
  currentRatios: {
    "PE_Shiller": 30.81,
    "PE_multpl": 28.16,
    "PE_investorsfriend": 17.00,
    "PE_fullratio": 39.85,
    "PE_HSI": 12.60
  },
  
  marketData: [
    {
      market: "S&P 500 (CAPE)",
      source: "Shiller",
      historical: 17.90,
      current: 30.81,
      change: 72.2,
      status: "高估",
      description: "Shiller CAPE 比率目前為30.81，比歷史平均值17.90高出72.2%。這一水平接近歷史高點，暗示市場可能存在泡沫風險。"
    },
    {
      market: "S&P 500",
      source: "multpl.com",
      historical: 15.50,
      current: 28.16,
      change: 81.7,
      status: "高估",
      description: "來自 multpl.com 的數據顯示更為極端的情況，當前本益比28.16比歷史平均值15.50高出81.7%。"
    },
    {
      market: "道瓊工業平均",
      source: "investorsfriend.com",
      historical: 20.10,
      current: 17.00,
      change: -15.4,
      status: "低估",
      description: "唯一顯示相對低估的主要美國指數，當前本益比17.00比歷史平均值20.10低15.4%。"
    },
    {
      market: "NASDAQ",
      source: "fullratio.com",
      historical: 29.56,
      current: 39.85,
      change: 34.8,
      status: "高估",
      description: "顯示出科技股的高估值特徵，當前本益比39.85比歷史平均值29.56高出34.8%。"
    },
    {
      market: "恒生指數",
      source: "HSI 數據",
      historical: 11.83,
      current: 12.60,
      change: 6.5,
      status: "輕微高估",
      description: "表現相對穩定，當前本益比12.60僅比歷史平均值11.83高出6.5%。"
    }
  ],
  
  insights: [
    {
      title: "美國市場普遍高估",
      content: "除道瓊工業平均指數外，美國主要股票市場普遍處於歷史高估值水平，要求投資者在配置資產時更加謹慎。"
    },
    {
      title: "估值差異提供機會",
      content: "不同市場間的估值差異為分散投資提供了機會。道瓊工業平均指數的相對低估值可能為價值投資者提供機會。"
    },
    {
      title: "亞洲市場相對穩定",
      content: "恒生指數的溫和估值水平可能為尋求國際多元化的投資者提供選擇。"
    }
  ],
  
  fearGreedIndex: {
    us: {
      value: 29,
      sentiment: "Fear",
      sentimentChinese: "恐懼",
      description: "美國市場當前處於恐懼狀態，投資者情緒偏向謹慎，可能為逢低買入的機會。",
      source: "CNN Fear & Greed Index",
      lastUpdated: "2025-10-11"
    },
    hk: {
      value: 66.56,
      sentiment: "Greed",
      sentimentChinese: "貪婪",
      description: "香港市場當前處於貪婪狀態，投資者情緒樂觀，建議謹慎評估風險。",
      source: "MacroMicro MM Hong Kong Fear & Greed Index",
      lastUpdated: "2025-10-03"
    }
  },

  fundFlows: {
    us: {
      lastUpdated: "2025-08-31",
      summary: "2025年8月，美國長期共同基金和交易所交易基金 (ETFs) 共流入770億美元，是自2025年2月以來最大的單月流入。應稅債券基金持續強勁，流入近650億美元。黃金持續受到青睞，流入約60億美元。美國股票基金在過去四個月流出近870億美元，其中增長型基金是主要原因，但被動型ETF仍有大量資金流入。",
      details: [
        { category: "長期共同基金和ETF", flow: "+770億美元", period: "2025年8月" },
        { category: "應稅債券基金", flow: "+650億美元", period: "2025年8月" },
        { category: "大宗商品基金 (黃金)", flow: "+60億美元", period: "2025年8月" },
        { category: "美國股票基金", flow: "-870億美元", period: "過去四個月" },
        { category: "增長型基金", flow: "-1000億美元", period: "過去一年" },
        { category: "大型混合型基金 (被動型ETF)", flow: "+2170億美元", period: "過去一年" }
      ],
      source: "Morningstar"
    },
    hk: {
      lastUpdated: "2025-10-10",
      summary: "香港交易所滬深港通數據顯示，2025年10月10日上海港股通成交額為1659.41億人民幣，其中多隻科技和金融股活躍。",
      shanghaiConnectNorthbound: {
        turnover: "1659.41億人民幣",
        trades: "676.86萬",
        dailyQuotaBalance: "可用",
        etfTurnover: "31.13億人民幣"
      },
      top10ActivelyTraded: [
        { rank: 1, code: "601899", name: "ZIJIN MINING", turnover: "42.64億人民幣" },
        { rank: 2, code: "601138", name: "FOXCONN INDUSTRIAL INTERNET", turnover: "27.52億人民幣" },
        { rank: 3, code: "688256", name: "CAMBRICON TECHNOLOGIES CORPORATION", turnover: "23.10億人民幣" },
        { rank: 4, code: "688041", name: "HYGON INFORMATION TECHNOLOGY", turnover: "21.75億人民幣" },
        { rank: 5, code: "603259", name: "WUXI APPTEC", turnover: "21.18億人民幣" },
        { rank: 6, code: "600036", name: "CHINA MERCHANTS BANK", turnover: "19.58億人民幣" },
        { rank: 7, code: "601127", name: "SERES GROUP", turnover: "18.94億人民幣" },
        { rank: 8, code: "601688", name: "HUATAI SECURITIES", turnover: "18.76億人民幣" },
        { rank: 9, code: "600519", name: "KWEICHOW MOUTAI", turnover: "18.59億人民幣" },
        { rank: 10, code: "688008", name: "MONTAGE TECHNOLOGY", turnover: "16.86億人民幣" }
      ],
      source: "HKEX Stock Connect"
    }
  },

  references: [
    {
      id: 1,
      title: "Robert Shiller, Yale University",
      url: "http://www.econ.yale.edu/~shiller/data.htm"
    },
    {
      id: 2,
      title: "Multpl.com - S&P 500 PE Ratio",
      url: "https://www.multpl.com/"
    },
    {
      id: 3,
      title: "InvestorsFriend.com - Dow Jones PE Ratio",
      url: "https://www.investorsfriend.com/"
    },
    {
      id: 4,
      title: "FullRatio.com - NASDAQ PE Ratio",
      url: "https://www.fullratio.com/"
    },
    {
      id: 5,
      title: "CNN Fear & Greed Index",
      url: "https://www.cnn.com/markets/fear-and-greed"
    },
    {
      id: 6,
      title: "MacroMicro - Hong Kong Fear & Greed Index",
      url: "https://en.macromicro.me/series/46930/hong-kong-mm-fear-and-greed-index"
    },
    {
      id: 7,
      title: "Morningstar - US Fund Flows",
      url: "https://www.morningstar.com/business/insights/blog/funds/us-fund-flows"
    },
    {
      id: 8,
      title: "HKEX - Historical Daily Stock Connect",
      url: "https://www.hkex.com.hk/Mutual-Market/Stock-Connect/Statistics/Historical-Daily?sc_lang=en"
    }
  ]
};

export const chartColors = {
  primary: "#2563eb",
  secondary: "#64748b",
  success: "#10b981",
  warning: "#f59e0b",
  danger: "#ef4444",
  info: "#06b6d4"
};
