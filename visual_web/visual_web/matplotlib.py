import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from .models import Post, Component, Line, Component, ProblemType
# models.py 에서 생성한 각 class를 불러온다


def matplotlib_graph(request):
    post_df = pd.DataFrame(list(Post.objects.all().values()))
    line_df = pd.DataFrame(list(Line.objects.all().values()))
    component_df =pd.DataFrame(list(Component.objects.all().values()))
    problem_df = pd.DataFrame(list(ProblemType.objects.all().values()))
    # 각 class에서 pandas로 데이터 뽑아오기

    post_df = post_df.merge(line_df, left_on='line_id', right_on='id', how = 'inner').drop(['id_x','id_y'],axis=1)
    post_df = post_df.merge(problem_df, left_on='problem_id', right_on='id', how = 'inner')
    df = post_df.merge(component_df, left_on='component_id', right_on='id', how = 'inner')
    # 각 Dataframe 합치기

    df_line_component = pd.DataFrame(df.groupby(['name_x']).count())
    # 데이터 가공

    plt.bar(df_line_component.index,df_line_component['name'])
    # plot

    plt.savefig('C:/Users/chongs/Desktop/production_meeting/django_project/image/graph/foo.png')
    # image 
