from langchain_core.tools import tool

@tool
def getWeather(city):
    """获取城市天气"""
    if city == "北京":
        return "北京天气晴朗"
    if(city == "上海"):
        return "上海天气阴天"
    return "未知城市"