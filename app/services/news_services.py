from app.views.news import News,request,db
def service_alter_news_information(news_id):
    if News.query.filter_by(id=news_id).first() is not None:
        data = request.get_json()
        news = News.query.get(news_id)

        news.title = data['title'] if data.get(
            'title') else news.title

        news.subtitle = data['subtitle'] if data.get(
            'subtitle') else news.subtitle

        news.content = data['content'] if data.get(
            'content') else news.content

        news.upvotes = data['upvotes'] if data.get(
            'upvotes') else news.upvotes

        news.downvotes = data['downvotes'] if data.get(
            'downvotes') else news.downvotes

        news.create_at = data['create_at'] if data.get(
            'create_at') else news.create_at

        news.approved = data['approved'] if data.get(
            'approved') else news.approved

        news.author = data['author'] if data.get(
            'author') else news.author

        db.session.commit()