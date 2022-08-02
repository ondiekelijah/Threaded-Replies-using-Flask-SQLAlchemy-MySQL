from app import create_app,db
from flask import current_app
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    flash,
    url_for,
    abort,
    send_from_directory,
)
from werkzeug.routing import BuildError
from sqlalchemy.exc import (
    IntegrityError,
    DataError,
    DatabaseError,
    InterfaceError,
    InvalidRequestError,
)
from models import Post,Comment
from forms import CommentForm,ReplyForm

app =  create_app()

@app.route("/", methods=("GET", "POST"), strict_slashes=False)
def index():

    # Uncomment the following line to INSERT a test post
    # Comment when you are done to avoid duplicate posts


    # If you're using this as an API, you'll want to create a new endpoint to handle the POST

    # p2 = Post(title='React,Sanity & Flask', body=
    #     """
    #     It would also be possible to avoid the double save if you come up with a different way 
    #     to generate auto-incrementing numbers, but that requires a very careful
    #     design to avoid race conditions, so I decided to stick with the double save solution.
    #     """
    # )
    # db.session.add(p2)
    # db.session.commit()

    posts = Post.query.order_by(Post.id.desc()).all()

    return render_template("index.html", posts=posts,title='Home')

@app.route("/<int:post_id>",methods=("GET", "POST"),strict_slashes=False)
def article(post_id):
    form = CommentForm()
    form2 = ReplyForm()
    
    post = Post.query.filter_by(id=post_id).first_or_404()
    comments = Comment.query.filter_by(post_id=post.id).order_by(Comment.path.asc())

    if request.method == 'POST' and form.validate_on_submit():

        author = form.author.data
        text = form.comment.data

        comment = Comment(
            text = text,
            author = author, 
            post_id = post.id,
        )

        comment.save()
        flash("Comment posted ", "success")


    return render_template('article.html',
        post=post,
        form1=form,
        form2=form2,
        comments=comments
        )



@app.route("/<int:post_id>/<int:comment_id>",methods=("GET", "POST"),strict_slashes=False)
def reply_comment(post_id,comment_id):

    form1 = CommentForm()
    form = ReplyForm()

    post = Post.query.filter_by(id=post_id).first_or_404()
    parent = Comment.query.filter_by(id=comment_id).first_or_404()
    comments = Comment.query.filter_by(post_id=post.id).order_by(Comment.path.asc())


    if request.method == 'POST' and form.validate_on_submit():

        author = form.author.data
        text = form.reply.data

        comment = Comment(
            parent = parent,
            text = text, 
            author = author, 
            post_id = post.id,
        )

        comment.save()
        flash("Reply posted ", "success")

    return render_template('article.html',
        post=post,
        form2=form,
        form1=form1,
        comments=comments
        )


if __name__ == "__main__":
    app.run(debug=True)
