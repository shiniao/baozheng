from django.http.response import Http404
from django.shortcuts import render
from .models import Source, Origin
import random


# Create your views here.

# 语料库列表
def index(request):
    origins = Origin.objects.all()

    for origin in origins:
        all_source = Source.objects.filter(origin_id=origin.id).count()
        completed = Source.objects.filter(origin_id=origin.id, marked=True).count()
        origin.percentage = f'{completed / all_source:.2}%'

    context = {'origins': origins}
    return render(request, 'mark/index.html', context)


# 语料库评判
def judge(request, origin_id):
    # * 从source 随机取一个
    # source = Source.objects.raw(
    #     'SELECT * FROM mark_source WHERE marked=false ORDER BY RANDOM() limit 1'
    # )
    # TODO 数据量大会有性能问题
    # source_list = [s.id for s in Source.objects.all().filter(marked=False)]
    # choice_source = random.choice(source_list)
    # source = Source.objects.get(pk=choice_source)

    # * 使用测试数据库
    # * 待优化
    source = Source.objects.raw(
        'SELECT * FROM mark_source WHERE marked=false AND origin_id=%s ORDER BY RAND() limit 1',
        [origin_id]
    )
    context = {'source': source[0]}
    return render(request, 'mark/judge.html', context)


def detail(request, source_id):
    try:
        source = Source.objects.get(pk=source_id)
    except Source.DoesNotExist:
        raise Http404("Source does not exist")
    return render(request, 'mark/detail.html', {'source': source})
