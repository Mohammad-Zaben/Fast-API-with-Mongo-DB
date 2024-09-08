from database import database


async def show_all_books():
    collections = database.books
    result = await collections.find({})
    return result


async def insert_book(book_data: dict):
    collections = database.books
    result = await collections.insert_one(book_data)
    return result.inserted_id
