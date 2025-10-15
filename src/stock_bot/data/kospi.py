from . import * 

async def get_kospi_list():
    """
    Fetches the list of KOSPI stocks and returns it as a formatted string for Discord.
    """
    print("Fetching KOSPI stock list...")
    try:
        # This is the core part that fetches the KOSPI list
        df_kospi = fdr.StockListing('KOSPI')
        
        print(df_kospi)

        # Keep only the essential columns for the display
        df_display = df_kospi[['Code', 'Name', 'Market', 'Close']].head(15) # Show top 15 stocks
        
        response_message = f"**KOSPI Stock List (Top 15)**\n"
        response_message += "```\n"
        response_message += df_display.to_markdown(index=False)
        response_message += "\n```"
        
        print(f"Successfully fetched and formatted {len(df_kospi)} KOSPI stocks.")
        return response_message
        
    except Exception as e:
        error_message = f"Failed to fetch KOSPI list: {e}"
        print(error_message)
        return error_message

## Embed 
# import pandas as pd
# import discord
# import FinanceDataReader as fdr
# from datetime import datetime

# async def get_kospi_list():
#     """
#     KOSPI 종목 리스트를 가져와 discord.Embed 객체로 만들어 반환합니다.
#     """
#     print("Fetching KOSPI stock list for Embed...")
#     try:
#         df_kospi = fdr.StockListing('KOSPI')
        
#         # 1. Embed 기본 틀 생성
#         embed = discord.Embed(
#             title="KOSPI 상장 기업 목록 (시가총액 상위 10개)",
#             description="한국 코스피 시장에 상장된 기업 목록입니다.",
#             color=discord.Color.blue(),
#             timestamp=datetime.now()
#         )

#         # 2. 데이터프레임의 각 행을 Embed의 필드로 추가
#         for index, row in df_kospi.head(10).iterrows():
#             embed.add_field(
#                 name=f"{index + 1}. {row['Name']}", 
#                 value=f"코드: {row['Code']}", 
#                 inline=False  # 각 항목이 한 줄을 모두 차지하도록 설정
#             )
            
#         embed.set_footer(text="Data provided by FinanceDataReader")
        
#         print("Embed created successfully.")
#         return embed

#     except Exception as e:
#         print(f"Failed to create embed: {e}")
#         embed = discord.Embed(
#             title="오류 발생",
#             description=f"KOSPI 목록을 가져오는 데 실패했습니다: {e}",
#             color=discord.Color.red()
#         )
#         return embed