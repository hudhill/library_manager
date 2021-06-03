import pdb
from models.book import Book
from models.author import Author
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author_1 = Author("Deborah", "Levy")
author_repository.save(author_1)
author_2 = Author("Ben", "Lerner")
author_repository.save(author_2)
author_3 = Author("Olga", "Tokarczuk")
author_repository.save(author_3)
author_4 = Author("Don", "DeLillo")
author_repository.save(author_4)
author_5 = Author("Nan", "Shepherd")
author_repository.save(author_5)

book_1 = Book("Hot Milk", author_1, 2016)
book_repository.save(book_1)
book_2 = Book("The Man Who Saw Everything", author_1, 2019)
book_repository.save(book_2)
book_3 = Book("10:04", author_2, 2014)
book_repository.save(book_3)
book_4 = Book("The Topeka School", author_2, 2019)
book_repository.save(book_4)
book_5 = Book("Drive Your Plow Over the Bones of the Dead", author_3, 2009)
book_repository.save(book_5)
book_6 = Book("White Noise", author_4, 1985)
book_repository.save(book_6)
book_7 = Book("Underworld", author_4, 1997)
book_repository.save(book_7)
book_8 = Book("The Living Mountain", author_5, 1977)
book_repository.save(book_8)

pdb.set_trace()
