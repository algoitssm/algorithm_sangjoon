from collections import defaultdict


def solution(genres, plays):
    answer = []

    dic = defaultdict(list)
    for i, genre in enumerate(genres):
        dic[genre].append((i, plays[i]))

    # 속한 노래가 많이 재생된 장르
    sorted_genre = sorted(dic.items(), key=lambda item: -
                          sum([x[1] for x in item[1]]))

    # 장르 내 많이 재생된 노래 & 재생횟수가 같을 경우 고유번호가 낮은 순
    for genre, tracks in sorted_genre:

        sorted_tracks = sorted(tracks, key=lambda x: (-x[1], x[0]))
        for i, t in sorted_tracks[:2]:
            answer.append(i)

    return answer
