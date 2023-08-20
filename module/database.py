import pymysql


class Database:
    def connect(self):

        return pymysql.connect(host="webscraper-mysql", user="root", password="admin", database="web_scrapping_db",
                               charset='utf8mb4')

    def read(self, image_name):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if image_name:
                cursor.execute("SELECT * FROM website_scrape_logs order by ingested_at desc")
            else:
                cursor.execute(
                    "SELECT * FROM website_scrape_logs where image_name = %s order by name desc", image_name)

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO website_scrape_logs"
                           "(image_name,total_downloads,total_stars,total_pulls) "
                           "VALUES(%s, %s, %s, %s)",
                           (data['image_name'], data['total_downloads'], data['total_stars'],
                            data['total_stars']))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def bulk_insert(self, data_tuple_arr):
        con = Database.connect(self)
        cursor = con.cursor()
        insert_query = "INSERT INTO website_scrape_logs"
        "(image_name,total_downloads,total_stars,total_pulls) "
        "VALUES(%s, %s, %s, %s)"
        try:
            cursor.executemany(insert_query, data_tuple_arr)
            con.commit()
            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def delete(self, image_name):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM website_scrape_logs where image_name = %s", (image_name,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()
