from django.shortcuts import render
from .forms import GroupForm  # フォームをインポート
from django.shortcuts import render

def shuffle_groups(request):
    # フォームが送信された場合
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            num_japanese = form.cleaned_data['num_japanese']
            num_foreign = form.cleaned_data['num_foreign']

            # ここで、実際に日本人と外国人の人数を使ってグループを作成します
            groups = []
            remaining_japanese = num_japanese
            remaining_foreign = num_foreign

            # グループ作成ロジック
            while (remaining_japanese > 0 or remaining_foreign > 0):
                # 各グループの人数を決める（最大4～5人）
                jp_in_group = min(remaining_japanese, 4)  # 日本人は最大4人
                fr_in_group = min(remaining_foreign, 2)  # 外国人は最大2人

                # もし、外国人が足りない場合は日本人を減らして調整
                if jp_in_group + fr_in_group > 5:
                    if fr_in_group > 0:
                        fr_in_group = 5 - jp_in_group
                    else:
                        jp_in_group = 5 - fr_in_group

                # グループを作成
                if jp_in_group > 0 and fr_in_group > 0:
                    groups.append({
                        'total': jp_in_group + fr_in_group,
                        'jp': jp_in_group,
                        'fr': fr_in_group,
                    })

                    # 残り人数を減算
                    remaining_japanese -= jp_in_group
                    remaining_foreign -= fr_in_group
                else:
                    break  # 日本人か外国人が足りなくなった場合に終了

            # あまり人数の計算
            remaining_japanese = remaining_japanese
            remaining_foreign = remaining_foreign

            # 結果を渡す
            return render(request, 'index.html', {
                'groups': groups,
                'remaining_japanese': remaining_japanese,
                'remaining_foreign': remaining_foreign,
                'form': form,  # フォームも再表示する
                'is_remaining': (remaining_japanese > 0 or remaining_foreign > 0),  # あまりがある場合
            })
    else:
        form = GroupForm()  # 初期表示の場合は空のフォーム

    return render(request, 'index.html', {'form': form})

def index(request):
    return render(request, 'index.html')