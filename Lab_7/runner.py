from tabulate import tabulate

from DAL.DataSaver import DataSaver
from Lab_7.APIClient import APIClient
from Lab_7.DataDisplay import DataDisplay
from Lab_7.ErrorHandler import ErrorHandler
from Lab_7.HistoryLogger import HistoryLogger
from UI.MenuItem import MenuItem
from UI.MenuBuilder import MenuBuilder

def run():
    client = APIClient()
    display = DataDisplay()
    saver = DataSaver()
    logger = HistoryLogger()

    def show_all_posts():
        try:
            posts = client.get_data("posts")
            display.show_table(posts)
            logger.log("показати всі пости", posts)
        except Exception as e:
            ErrorHandler.handle_error(e)

    def show_post_by_id():
        try:
            post_id = input("Введіть ID поста: ")
            post = client.get_data_by_id("posts", post_id)
            display.show_table([post])
            logger.log(f"показати пост з ID {post_id}", post)
        except Exception as e:
            ErrorHandler.handle_error(e)

    def save_data():
        format_choice = input("Введіть формат збереження (json/csv/txt): ").strip().lower()
        filename = input("Введіть ім'я файлу: ").strip()
        if format_choice in ['json', 'csv', 'txt']:
            try:
                saver_method = {
                    'json': saver.save_as_json,
                    'csv': saver.save_as_csv,
                    'txt': saver.save_as_txt
                }[format_choice]
                posts = client.get_data("posts")  # Fetch posts before saving
                saver_method(posts, filename)
                print(f"Дані збережено у {filename}.{format_choice}")
            except Exception as e:
                ErrorHandler.handle_error(e)
        else:
            print("Невідомий формат.")

    def show_all_users():
        try:
            users = client.get_all_users()
            display.show_users(users)
            logger.log("показати всіх користувачів", users)
        except Exception as e:
            ErrorHandler.handle_error(e)

    def show_user_by_id():
        try:
            user_id = input("Введіть ID користувача: ")
            user = client.get_user_by_id(user_id)
            display.show_users([user])
            logger.log(f"показати користувача з ID {user_id}", user)
        except Exception as e:
            ErrorHandler.handle_error(e)

    def show_all_comments():
        try:
            comments = client.get_all_comments()
            display.show_comments(comments)
            logger.log("показати всі коментарі", comments)
        except Exception as e:
            ErrorHandler.handle_error(e)

    def show_comment_by_id():
        try:
            comment_id = input("Введіть ID коментаря: ")
            comment = client.get_comment_by_id(comment_id)
            display.show_comments([comment])
            logger.log(f"показати коментар з ID {comment_id}", comment)
        except Exception as e:
            ErrorHandler.handle_error(e)

    def show_history():
        logger.show_history()

    def exit_program():
        print("Вихід...")
        return

    menu_items = [
        MenuItem("1", "Показати всі пости", show_all_posts),
        MenuItem("2", "Показати пост за ID", show_post_by_id),
        MenuItem("3", "Зберегти дані", save_data),
        MenuItem("4", "Показати всіх користувачів", show_all_users),
        MenuItem("5", "Показати користувача за ID", show_user_by_id),
        MenuItem("6", "Показати всі коментарі", show_all_comments),
        MenuItem("7", "Показати коментар за ID", show_comment_by_id),
        MenuItem("8", "Показати історію", show_history),
        MenuItem("0", "Вийти", exit_program),
    ]

    menu = MenuBuilder(menu_items)
    while True:
        menu.initialize()
