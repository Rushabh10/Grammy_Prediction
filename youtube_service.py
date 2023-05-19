from typing import Generator
from typing import List
from datetime import datetime
from datetime import timezone
from googleapiclient.discovery import build
from rich.console import Console



Comments = List[str]
CommentGenerator = Generator[Comments, None, None]


class YoutubeService:
    """Handle API requests

    https://developers.google.com/youtube/v3/docs/videos
    https://developers.google.com/youtube/v3/docs/commentThreads
    https://github.com/youtube/api-samples/blob/master/python/comment_handling.py

    :type video_url: str
    :param video_url: URL of the video
    """

    def __init__(self, video_url: str, key:str) -> None:
        self.api_key = key
        self._video_url = video_url
        self._video_id = video_url.split("?v=")[1]
        self._service = build('youtube','v3',developerKey = self.api_key)

    def get_comment_threads(self, include_replies: bool = False, year: str = "2023") -> CommentGenerator:
        """Get the top level comments. If --include_replies option is given,
        also get the replies of the top level comments.

        :type include_replies: bool
        :param include_replies: Whether reply comments will be included or not
        :rtype: CommentGenerator
        :returns: List of comments
        """

        console = Console()

        with console.status(f"[bold bright_green]Getting comments for video: {self._video_url}"):


            results = (
                self._service.commentThreads()
                .list(
                    part="snippet", videoId=self._video_id, textFormat="plainText", maxResults=100
                )
                .execute()
            )

            while results:

                for comment_thread in results["items"]:
                    comment = comment_thread["snippet"]["topLevelComment"]
                    comment_text = comment["snippet"]["textDisplay"]
                    timestamp = datetime.fromisoformat(comment['snippet']['publishedAt'][:-1] + '+00:00')
                    start = datetime.fromisoformat(str(int(year)-2)+'-10-01T00:00:00.000Z'[:-1] + '+00:00')
                    end = datetime.fromisoformat(str(int(year)-1)+'-09-30T00:00:00.000Z'[:-1] + '+00:00')
                    if(start <= timestamp and timestamp <= end):
                        yield comment_text.replace(',','').replace('\n','')+','+comment['snippet']['publishedAt']

                    reply_count = comment_thread["snippet"]["totalReplyCount"]

                    if include_replies and reply_count > 0 and (start <= timestamp and timestamp <= end):

                        replies = self._get_comment_replies(comment_thread["id"])

                        # replies are returned in reverse order!
                        for reply in reversed(replies):
                            reply_text = reply["snippet"]["textDisplay"]

                            if start <= timestamp and timestamp <= end:
                                yield reply_text.replace(',','').replace('\n','')+","+comment['snippet']['publishedAt']

                if "nextPageToken" in results:
                    results = (
                        self._service.commentThreads()
                        .list(
                            part="snippet",
                            videoId=self._video_id,
                            textFormat="plainText",
                            pageToken=results["nextPageToken"],
                            maxResults=100,
                        )
                        .execute()
                    )
                else:
                    break

    def get_video_title(self) -> str:
        """Get the title of the video

        :rtype: str
        :returns: Video title
        """

        response = self._service.videos().list(part="snippet", id=self._video_id).execute()

        return response["items"][0]["snippet"]["title"]

    def _get_comment_replies(self, comment_id: str) -> Comments:
        """Get the replies to the comment given by id

        :type comment_id: str
        :param comment_id: Id of parent comment
        :rtype: Comments
        :returns: List of reply comments
        """

        results = (
            self._service.comments()
            .list(
                part="snippet",
                parentId=comment_id,
                textFormat="plainText",
            )
            .execute()
        )

        return results["items"]
