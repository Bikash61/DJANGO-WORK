from django.shortcuts import render
from .models import CoalMine, Tree



def add_mine(request):
    if request.method == 'POST':
        form = CoalMineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CoalMineForm()
    return render(request, 'emissions/add_mine.html', {'form': form})


def add_tree(request):
    if request.method == 'POST':
        form = TreeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TreeForm()
    return render(request, 'emissions/add_tree.html', {'form': form})




def dashboard(request):
    coal_mines = CoalMine.objects.all()
    trees = Tree.objects.all()

    coal_mines_data = []
    for mine in coal_mines:
        tree_data = []
        for tree in trees:
            trees_needed = mine.trees_needed_to_offset(tree.carbon_absorption_rate)
            tree_data.append({
                'name': tree.name,
                'trees_needed': trees_needed
            })
        coal_mines_data.append({
            'name': mine.name,
            'emissions': mine.calculate_emissions(),
            'trees': tree_data
        })

    context = {
        'coal_mines_data': coal_mines_data,
    }

    return render(request, 'emissions/dashboard.html', context)
