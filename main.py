from fastapi import FastAPI,Body, Depends
from app.model import PostSchema,UserLoginSchema,UserSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearner

posts = [
    {
        "id" : 1,
        "title": "penguis",
        "text":  "penguins are the group of aquatic flightless birds. "
    },
    {
        "id" : 2,
        "title": "tiger",
        "text":  "Tigers are the largest living cat spices and a membersof the genus panthera. "
    },
    {
        "id" : 3,
        "title": "koalas",
        "text":  "koalas is arboreal herbivours marsupial marsupial native to Australia"
    }
    
]


users = []


app = FastAPI()


# Get - for testing
@app.get("/", tags=["test"])
async def greet():
    return {'Hello': "World"}

# Get Posts
@app.get("/post", tags=["posts"])
async def get_post():
    return {"daata" : posts}

#Get Single post {id}
@app.get("/post/{id}", tags=["posts"])
async def get_one_post(id : int):
    if id > len(posts):
        return {
            "error": "Post with this id does not Exists!"
        }
    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }
        
#4 Post a blog post  [A handler for creating a post]
@app.post("/posts", dependencies=[Depends(jwtBearner())], tags=["posts"])
async def add_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "info": "Post Added!"
    }

#5 User Signup [ Create New User ]
@app.post("/user/signup", tags=["user"])
async def user_signup(user: UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False
    
@app.post("/user/login", tags=["user"])
async def user_login(user: UserLoginSchema = Body(default = None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            "error" : "Invalid login details!"
        }
    
