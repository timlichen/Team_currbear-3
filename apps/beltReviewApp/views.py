from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Review, Author, Book



def specificReview(request):
	if Review.ReviewManager.createReview(request.POST, request):

		return render(request, ('beltreviewtemplates/show.html'))



def bookReview(request):
	# this is invalid syntax
	# data = {request.POST
	# id = request.session
	# }

	if Review.ReviewManager.isValid(data):
		Review.ReviewManager.createReview(data)
		print "here"
		# return redirect(reverse('my_specific_review'))
		return render(request, ('beltreviewtemplates/show.html'))
	# else:

		# redirect(reverse('my_book_review'))
