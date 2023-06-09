from django.shortcuts import render, redirect
from .models import Todolist
from datetime import datetime, timedelta, date
# Create your views here.
def main(request):
    todolists = Todolist.objects.all()
    today=date.today()
    return render(request, 'main.html', {'todolists':todolists, 'today':today})

def new(request):
    if request.method =='POST':
        #due가 자꾸 값이 비어있으면 오류가 나서,기본값으로 1주일의 시간을 주기로 했음
        if request.POST['due']=="":
            w=timedelta(weeks=1)
            due_result=datetime.now()+w
        else :
            due_result=request.POST['due']
        new_todolist=Todolist.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            status=request.POST['status'],
            due=due_result,
            created_at=datetime.now()
        )

        return redirect('detail', new_todolist.id)
    return render(request, 'new.html')

def detail(request, todolist_id):
    todolist=Todolist.objects.get(id=todolist_id)
    return render(request, 'detail.html',{'todolist':todolist})

def update(request, todolist_id):
    todolist=Todolist.objects.get(id=todolist_id)

    if request.method =='POST':
        #due가 자꾸 값이 비어있으면 오류가 나서,기본값으로 1주일의 시간을 주기로 했음
        if request.POST['due']=="":
            w=timedelta(weeks=1)
            due_result=datetime.now()+w
        else :
            due_result=request.POST['due']
        Todolist.objects.filter(id=todolist_id).update(
                title=request.POST['title'],
                content=request.POST['content'],
                status=request.POST['status'],
                due=due_result,
                rewrited_at=datetime.now()

        )
        return redirect('detail', todolist_id)
    return render(request, 'update.html',{'todolist':todolist})

def delete(request, todolist_id):
    todolist=Todolist.objects.get(id=todolist_id)
    todolist.delete()
    return redirect('/')