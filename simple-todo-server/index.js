const express = require ("express");
const app = express();


const users=[{
    name:"Rohan",
    todos:[{
        complete:true,
        
    }]
    
}];
app.use(express.json());



// route handlers



// main todo backend  code..........................................................

//for get request  write a logic to show number of todos,nymber of completed and number of incomplete todos
app.get("/",function(req,res){

    const rohantodos = users[0].todos;
    const numberOfTodos = rohantodos.length;
    let numberOfCompleteTodos = 0;
    for(let i=0;i<rohantodos.length;i++){
        if(rohantodos[i].complete){
            numberOfCompleteTodos = numberOfCompleteTodos+1;
        }
    }
    const numberOfIncompleteTodos = numberOfTodos - numberOfCompleteTodos;
    res.json({
        numberOfTodos,
        numberOfCompleteTodos,
        numberOfIncompleteTodos
    })
})

//for post request send data in body for adding a new todo 
app.post("/",function(req,res){

    const doneCheck= req.body.doneCheck;
    users[0].todos.push({
        complete:doneCheck
    })
    res.json({
        msg:"added!"
    });
})

// for put request user can replace an incomplete todo with complete todo
app.put("/",function(req,res){

    if(AtleastOneincomplete()){
        for(let i=0;i<users[0].todos.length;i++){
            users[0].todos[i].complete = true;
        }
        res.json({});

    }
    else{
        res.status(411).json({
            msg:"Bro your all tasks are complete"
        })
    }
})
// for delete request user can remove incomplete todo
app.delete("/",function(req,res){
    if(AtleastOneincomplete()){
        const newTodos = [];
        for(let i=0;i<users[0].todos.length;i++)
        {
            if(users[0].todos[i].complete){
                newTodos.push({
                    complete:true
                })
            }
            users[0].todos= newTodos;

        }
        res.json({
            msg:"bhadve kar diya delete."
        })
    }
    else{
        //res.sendStatus(411); or
        res.status(411).json({
            msg:"You have no incomplete todos"
        })
    }
})

// incomplete todo check function 
function AtleastOneincomplete(){
    let atleastOneIncompleteTodo = false;
    for(let i=0;i<users[0].todos.length;i++)
    {
        if(!users[0].todos.complete){
            atleastOneIncompleteTodo = true;
        }

    }
    return atleastOneIncompleteTodo;

}
//port
app.listen(3000);

