from django.shortcuts import render
# from django.http import JsonResponse
import coreapi


# Create your views here.

def test(request, *args, **kwargs):
    client = coreapi.Client()
    schema = client.get('http://127.0.0.1:8080/medias/')

    my_context = {
        "schema": schema
    }
    return render(request, "album.html", my_context)

    # return JsonResponse(schema, safe = False)


'''
[{"id": 1, "topic": {"id": 1, "name": "Corona"}, "title": "Unlock 3.0", "description": "Very very very interesting", "file": "media/admin/20-07/78b42b11-3d5c-49d8-9ec2-62b0463c5360.jpg", "tags": "corona, unlock, lockdown", "author": 1}, {"id": 2, "topic": {"id": 2, "name": "abcd"}, "title": "some title", "description": "eggadgadf", "file": null, "tags": "", "author": 1}, {"id": 3, "topic": {"id": 2, "name": "abcd"}, "title": "no title", "description": "saffada", "file": null, "tags": "", "author": 2}, {"id": 4, "topic": {"id": 3, "name": "forest"}, "title": "Tropical Forest", "description": "classification of forests", "file": null, "tags": "", "author": 2}]
'''
