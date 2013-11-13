# coding: utf8
# try something like
@auth.requires_login()
def new():
    form=SQLFORM(db.request_book)
    if form.process(dbio=False).accepted:
        # check in published books and email
        db.request_book.insert(auth_user=auth.user.id,  **dict(form.vars))
        response.flash="request success"
    else:
        response.flash="error in form"
    return dict(form=form)
