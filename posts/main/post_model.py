class PostModel:
    def __init__(self, pk=0, content="", pic="", poster_avatar="", poster_name="", views_count=0, likes_count=0):
        self.pk = pk
        self.content = content
        self.pic = pic
        self.poster_avatar = poster_avatar
        self.poster_name = poster_name
        self.views_count = views_count
        self.likes_count = likes_count

    def as_dict(self):
        post_dict = {
            "pk": self.pk,
            "content": self.content,
            "pic": self.pic,
            "poster_avatar": self.poster_avatar,
            "poster_name": self.poster_name,
            "views_count": self.views_count,
            "likes_count": self.likes_count,
        }

        return post_dict

    def __repr__(self):
        return f"Post({self.pk}, {self.poster_name}, " \
               f"{self.poster_avatar}, {self.pic}, {self.content}, {self.views_count}, {self.likes_count})"