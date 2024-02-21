from django.shortcuts import render
import requests
import pickle
from django.http import JsonResponse



def home(request):
    return render(request,"mrs_backend/home.html")



# def recommendColla(request, item_id):

    
#     res = recommendMovie(item_id)
#     print(res.text)


#     return render(request, "mrs_backend/recommendation.html")



def recommendMovie(request, movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NWVlMjFmN2NkZjhkMDdhNmQxYmI0NjU3OGJlYmQwNiIsInN1YiI6IjY1NDExNmQ2NmNhOWEwMDBjYTE1Yjk3MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.SD4zSAm3hDxAM2lnmJ_0DGrhEG9fnBBA2G5re6bP4sE"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()  # Convert response to JSON
        trimmed_data = data['results'][:5]
        return JsonResponse(trimmed_data, safe=False)
    else:
        # Return appropriate error response
        return JsonResponse({'error': 'Failed to fetch movie recommendations'}, status=500)
        



def recommendTV(request, tv_id):
    url = f"https://api.themoviedb.org/3/tv/{tv_id}/recommendations?language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NWVlMjFmN2NkZjhkMDdhNmQxYmI0NjU3OGJlYmQwNiIsInN1YiI6IjY1NDExNmQ2NmNhOWEwMDBjYTE1Yjk3MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.SD4zSAm3hDxAM2lnmJ_0DGrhEG9fnBBA2G5re6bP4sE"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()  # Convert response to JSON
        trimmed_data = data['results'][:5]
        return JsonResponse(trimmed_data, safe=False)
    else:
        # Return appropriate error response
        return JsonResponse({'error': 'Failed to fetch movie recommendations'}, status=500)
    # return response