Test task: python developer
Object of this task is to create a simple REST API. You can use one framework from this list (Django Rest Framework, Flask or FastAPI) and all libraries which you are prefer to use with this frameworks.

1. Social Network

Basic models:
● User
● Post (always made by a user)
Basic Features:
● user signup
● user login
● post creation
● post like
● post unlike
● analytics about how many likes was made. Example url
/api/analitics/?date_from=2020-02-02&date_to=2020-02-15 . API should return analytics aggregated by day.
● user activity an endpoint which will show when user was login last time and when he mades a last request to the service.

Requirements:
● Implement token authentication (JWT is prefered)
Object of this bot demonstrate functionalities of the system according to defined rules. This bot
should read rules from a config file (in any format chosen by the candidate), but should have
following fields (all integers, candidate can rename as they see fit).

# Social Network is created using Django Rest Framework
To start app you need to run migrations and run app in development mode

# Endpoints
## Create user
POST api/v1/account/
- required fields [ username: str, password: str ]
- response { email: str, username: str, id: int }

## Obtain JWT Token
POST api/v1/token/
- required fields [ username: str, password: str ]
- response { refresh: str, access: str }

## Create Post
POST api/v1/post/
### Authorization required
- required fields [ title: str, description: str, text: str]
- response { title: str, description: str, text: str, id: int }

## Like Post
PATCH api/v1/post/{post_id: int}
### Authorization required
- required fields [is_like: bool] True for like False for dislike
- response { None }

## Like Analytics
GET api/v1/post/analytics/
### Authorization required
- additional parameters [date_from: str, date_to: str] //?date_from=2021-01-24&date_to=2021-01-26
- response [ { like_date: str, likes: int }, ]

## User Analytics
GET api/v1/post/account/{account_id: int}/activity/
### Authorization required
- response { username: str, last_login: datetime,  last_visit: datetime}