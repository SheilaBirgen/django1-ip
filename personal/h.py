def search(request):
    '''View function to search by category'''
    template = loader.get_template('search.html')
    if 'image' in request.GET and request.GET['image']:
        search_category = request.GET['image']
        searched_images = Image.search_images(search_category)
        message = f'{search_category}'

        context = {
            'message': message,
            'images': searched_images,
        }
        return HttpResponse(template.render(context,request))

    else:
        message = 'The category does not exist!!'

        context = {
            'message': message,
        }
        return render(request, 'search.html', {'message': message})