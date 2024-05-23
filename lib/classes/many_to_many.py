class Article:
    all = [] # class attribute, keeps list of 'all' Article instances.
    
    def __init__(self, author, magazine, title):
        if isinstance(author, Author) and isinstance(magazine, Magazine):
            if isinstance(title, str) and (5 <= len(title) <= 50):
                self._author = author
                self._magazine = magazine
                self._title = title
                author._articles.append(self)
                magazine._articles.append(self)
                Article.all.append(self) # keeps track of 'all' instances of 'Article' class. 
                                         # executes bonus intruction => 'hint: needs a way to remember all mag objects.'
            else:
                raise ValueError("Title must be a string with length between 5 and 50 characters.")
        else:
            raise ValueError("Invalid author or magazine.")
                
    @property        # @property decorator to access 'title' attribute. Same for 'author' and 'magazine.
    def title(self):
        return self._title
    
    @title.setter    # @title.setter to control/ redefine 'title' attribute when assigned new vaule. Same for 'author' and 'magazine.
    def title(self, new_title):  # accepts 'new_title' param as new value.
            if hasattr(self, '_title'):  # 'hasattr()' checks if 'self' already has attr called '_title', hasattr returns True if does exist, if not- False.
                return
            if isinstance(new_title, str) and (5<= len(new_title) <= 50): # checks if 'new_title' is a string and the length is btwn 5 and 50 chars, inclusive.
                self._title = new_title                                   # if this checks out, assigns 'new_title' to attr '_title', to update the instance title.
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
            
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        
class Author:
    def __init__(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string.")
        self._articles = []
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        return 

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        if isinstance(magazine, Magazine) and isinstance(title, str) and (5 <= len(title) <= 50):
            new_article = Article(self, magazine, title)
            return new_article

    def topic_areas(self):
        categories = {article.magazine.category for article in self._articles}
        return list(categories) if categories else None

class Magazine:
    all =[]
    
    def __init__(self, name, category):
        if isinstance(name, str) and (2 <= len(name) <= 16):
            self._name = name
        else:
            raise ValueError("Name must be a string with length between 2 and 16 characters.")
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Category must be a non-empty string.")
            
        self._articles = []
        Magazine.all.append(self)
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and (2 <= len(new_name) <= 16):
            self._name = new_name
        else:
            raise ValueError("Name must be a string with length between 2 and 16 characters.")
            
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category
        else:
            raise ValueError("Category must be a non-empty string.")

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        titles = [article.title for article in self._articles]
        return titles if titles else None

    def contributing_authors(self):
        author_count = {}       # initializes empty dict, keeps track of how many articles each author contributed to mag. 
                                # 'authors' are keys, values are artilce counts.
        for article in self._articles:  # iterates over each article in '_articles' list.
            author = article.author   # gets author of curr article
            author_count[author] = author_count.get(author, 0) + 1  # updates 'author_count' for curr author. 'get()' gets count of articles by the author, defaults to 0, then increments by 1.
        qualifying_authors = [author for author, count in author_count.items() if count > 2]  # identifies qualifying authors. After loop, this makes a list of authors that contributed more than 2 articles to the mag. 
                                                                                              # iterates over 'items()' of 'suthor_count' (key val pairs of authors and article counts).
                                                                                              # 'if count > 2' filters out authors who contributed 2 or less articles.
        return qualifying_authors if qualifying_authors else None   # returns list of qualifying authors if any, if not returns 'None'.
    
    @classmethod
    def top_publisher(cls):
        if not cls.all or not Article.all: # checks if 'all (mag)' or 'Article.all' is empty
            return None
        return max(cls.all, key=lambda magazine: len(magazine.articles())) # 'max' determines which mag has most articles. 'cls.all' contains all mag class instances.
                                                                           # 'key=lambda' function that takes in mag and returns num of articles in mag.
                                                                           # this is done by calling 'articles()' method of each mag, returns a list of articles, then passes to 'len' to determine the size.
                                                                           # 'max' then compares lengths and returns mag with most articles.
                