import sqlite3
import statistics


conn = sqlite3.connect('database.db')
cursor = conn.cursor()


median_query = """
    SELECT country, 
           CAST(daily_vaccinations AS INTEGER) AS daily_vaccinations
    FROM country_vaccination_stats
    WHERE daily_vaccinations IS NOT NULL
"""

try:
    
    cursor.execute(median_query)
    medians = cursor.fetchall()

 
    country_medians = {}
    for country, daily_vaccinations in medians:
        if country not in country_medians:
            country_medians[country] = []
        country_medians[country].append(daily_vaccinations)

   
    for country, vaccinations in country_medians.items():
        median_value = statistics.median(vaccinations)

        
        update_query = """
            UPDATE country_vaccination_stats
            SET daily_vaccinations = ?
            WHERE country = ?
              AND (daily_vaccinations IS NULL OR daily_vaccinations = 0)
        """
        cursor.execute(update_query, (median_value, country))

    
    conn.commit()
    print("Eksik günlük aşılama numaraları başarıyla dolduruldu.")
except Exception as e:
    print("Hata:", e)
    conn.rollback()
finally:
    
    conn.close()
