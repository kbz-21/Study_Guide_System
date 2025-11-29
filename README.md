-  STUDY GUIDE SYSTEM PROJECT 
-  API end point functinality Testing(using postman)
-  This system also configured swagger for seeing easly the end points.

.........................................................................
USERS APP       1st 
.........................................................................
1.http://127.0.0.1:8000/api/v1/auth/register/    
  - function:  register new user
  - method - POST
  - body

 {
  "username": "jerry",
  "email": "jerry1921@gmail.com",
  "password": "pass123",
  "first_name": "Test",
  "last_name": "User"

  }



2. http://127.0.0.1:8000/api/v1/auth/login/
   - function: if user is registered can login 
   - method - POST
   - body

{
  "username_or_email": "jerry",
  "password": "pass123"
}


3. http://127.0.0.1:8000/api/v1/auth/logout/
   - function: a logged in user can log out from the system.
   - method - POST
   - key : Authentication  , value : Token <your tooken>


   AGAIN LOG IN BECAUSE NO YOU HAVE LOGGED OUT...


4. http://127.0.0.1:8000/api/v1/auth/profile/
   - function:
   - method - GET

 OUTPUT EXPECTED

   {
    "id": 5,
    "username": "kal",
    "email": "kalzed1921@gmail.com",
    "first_name": "Test",
    "last_name": "User",
    "profile_info": ""
   }


.........................................................................................
NOTE APP            2nd 
.........................................................................................

5. http://127.0.0.1:8000/api/v1/notes/
   - function: user can create notes
   - method - POST
   - body

   {
    "title": "My First Note",
    "content": "This is a test note for the Study Guide System."
   }

  OUTPUT EXPECTED

   {
    "id": 2,
    "title": "My First Note",
    "content": "This is a test note for the Study Guide System.",
    "created_at": "2025-10-14T12:56:15.806154Z",
    "updated_at": "2025-10-14T12:56:15.806212Z",
    "is_archived": false
   }


6. http://127.0.0.1:8000/api/v1/notes/
   - function: user can see his personal created notes
   - method - GET
   - Body (empty)

 OUTPUT EXPECTED
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "My First Note",
            "content": "This is a test note for the Study Guide System.",
            "created_at": "2025-10-14T12:41:31.729137Z",
            "updated_at": "2025-10-14T12:41:31.729179Z",
            "is_archived": false
        },
        {
            "id": 2,
            "title": "My First Note",
            "content": "This is a test note for the Study Guide System.",
            "created_at": "2025-10-14T12:56:15.806154Z",
            "updated_at": "2025-10-14T12:56:15.806212Z",
            "is_archived": false
        },

    ]
}



7. http://127.0.0.1:8000/api/v1/notes/3   
   - function: user can see his specific (single) notes by refering id
   - method - GET

OUTPUT EXPECTED

{
    "id": 3,
    "title": "My First Note",
    "content": "This is a test note for the Study Guide System.The tester name is kaleab zewdie
     an alx back end learner.this is last week for graduation and finalproject is goin to done 
     for graduation purpose.and show case our skill what we have learned.",
    "created_at": "2025-10-14T18:00:59.885404Z",
    "updated_at": "2025-10-14T18:00:59.885442Z",
    "is_archived": false
}


8. http://127.0.0.1:8000/api/v1/notes/3/
   - function: user update notes
   - method - PUT
   - body  
   {
    "title": "Updated Note",
    "content": "This is an updated test note."
   }

......


9. http://127.0.0.1:8000/api/v1/notes/3/archive/
   - function: Archive a Note
   - method - PATCH
   - body  - empty


OUTPUT EXPECTED


{
    "id": 3,
    "title": "Updated Note",
    "content": "This is a test note for the Study Guide System. The tester name is kaleab zewdie
    an alx back end learner. This is last week for graduation and final project is goin to done for graduation
    purpose. and show case our skill what we have learned.",
    "created at": "2025-10-14T18:00:59.885404Z",
    "updated at": "2025-10-14T19:08:27.826752Z",
    "is archived": true
}



10. http://127.0.0.1:8000/api/v1/notes/1/
   - function: user  delete notes
   - method - DELETE
   - body - empty

OUTPUT EXPECTED 

[]


.........................................................................................
TO DO LIST APP          3rd 
.........................................................................................

11.http://127.0.0.1:8000/api/v1/todolist/
   - function: user Create personal To-Do 
   - method - POST
   - body  - 
   {
    "title": " 12:00 ",
    "description": " weakup and take shower, then wear uniform "
    }


12. http://127.0.0.1:8000/api/v1/todolist/
   - function: List all availabe To-Dos
   - method - GET
   - body  - empty

13. http://127.0.0.1:8000/api/v1/todolist/1/

   - function: Retrieve to-do's by id
   - method - GET
   - body  - empty

14. http://127.0.0.1:8000/api/v1/todolist/1/
   - function: Update To Do list single task
   - method - PUT
   - body  -
    {
    "title": "Study Advanced Python",
    "description": "Focus on DRF serializers"
    }


15. http://127.0.0.1:8000/api/v1/todolist/1/complete/
   - function:  Mark Complete if the task is done
   - method - PATCH
   - body  - empty

16. http://127.0.0.1:8000/api/v1/todolist/1/

   - function: Delete single task by selecting it's id
   - method - DELETE
   - body  - empty


.........................................................................................
UNIT CONVERTER APP              4th
.........................................................................................


17. http://127.0.0.1:8000/api/v1/unitconverter/convert/
   - function:  perform conversion
   - method - POST
   - body  - 
   {
    "value": 10,
    "from_unit": "yard",
    "to_unit": "foot"
   }


   



other unit testing
   {
    "value": 5,
    "from_unit": "pound",
    "to_unit": "kilogram"
   }


18. http://127.0.0.1:8000/api/v1/unitconverter/history/
   - function: List Conversion History
   - method - GET
   - body  - empty


19. http://127.0.0.1:8000/api/v1/unitconverter/history/1/
   - function: user can see single conversion history using specific id
   - method - GET
   - body  - empty


.........................................................................................
YOUTUBE SEARCH APP              5th
.........................................................................................



20.  http://127.0.0.1:8000/api/v1/youtubesearch/search/   
   - function: user can search youtube video's using queries...
   - method - POST
   - body  - 

   {
    "q": "python tutorial"
   }


	OUTPUT ("10 searches will fetch from youtube and " )

        {
            "video_id": "K5KVEU3aaeQ",
            "title": "Python Full Course for Beginners [2025]",
            "channel": "Programming with Mosh",
            "thumbnail": "https://i.ytimg.com/vi/K5KVEU3aaeQ/hq720.jpg?sqp=-   				oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAXbPvWkQhvRSOYWD6mp9EVbfWSYg",
            "published_at": "8 months ago",
            "url": "https://www.youtube.com/watch?v=K5KVEU3aaeQ"
        },
.

21. http://127.0.0.1:8000/api/v1/youtubesearch/history/
   - function: user can see his previous search history
   - method - GET
   - body  -  empty


output .. history becomes listed