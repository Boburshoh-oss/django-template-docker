from django.conf import settings
from django.db import connection
from django.contrib import messages


class CatchRaisedRedirectMiddleware(object):
    MAX_RETRIES = 3

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        response = self.get_response(request)
        if settings.DEBUG:
            max_query = 20
            count_q = len(connection.queries)
            print(">>> QUERIES COUNT: ", count_q)
            if request.path.startswith("/references/api/v1/") and request.method in ["GET"]:
                for query in connection.queries:
                    print(">>> QUERY: ", query)
            if count_q > max_query:
                messages.warning(
                    request,
                    f"Queries count is {count_q}. Max query count is {max_query}. Please reduce!",
                )

            max_query_time = 0.5
            total_query_time = sum(float(query["time"]) for query in connection.queries)
            if total_query_time > max_query_time:
                messages.warning(
                    request,
                    f"Request queries execution time is {total_query_time}. "
                    f"Max query time is {max_query_time}. Please reduce!",
                )
        return response