from dataclasses import dataclass


@dataclass
class Track:
    title: str
    artist: str
    _duration_sec: int  # encapsulated

    @property
    def duration_sec(self) -> int:
        return self._duration_sec

    @duration_sec.setter
    def duration_sec(self, value: int) -> None:
        if value <= 0:
            raise ValueError("Duration should be above zero (sec)")
        self._duration_sec = value

    @staticmethod
    def format_duration(seconds: int) -> str:
        """Formats duration"""
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes}:{secs:02d}"

    def __str__(self) -> str:
        formatted_time = self.format_duration(self._duration_sec)
        return f"{self.artist} - {self.title} ({formatted_time})"


class Playlist:
    def __init__(self, name: str) -> None:
        self.name = name
        self._tracks: list[Track] = []

    def add_track(self, track: Track) -> None:
        """Adds track to list"""
        self._tracks.append(track)

    def remove_track(self, track: Track) -> None:
        """Removes track from list"""
        self._tracks = [item for item in self._tracks if item.title != track.title]

    def get_tracks(self) -> list["Track"]:
        """Returns list of Tracks"""
        return self._tracks

    @property
    def total_duration(self) -> int:
        return sum(track.duration_sec for track in self._tracks)

    @property
    def track_count(self) -> int:
        return len(self._tracks)

    @staticmethod
    def format_playlist_info(playlist: "Playlist") -> str:
        """Returns formatted playlist info"""
        duration_str = Track.format_duration(playlist.total_duration)
        lines = [
            f"Playlist: {playlist.name} (Tracks: {playlist.track_count}, time: {duration_str})"
        ]
        for track in playlist.get_tracks():
            lines.append(f"{track}")
        return "\n".join(lines)


class MusicLibrary:
    def __init__(self) -> None:
        self._playlists: list[Playlist] = []

    def add_playlist(self, playlist: Playlist) -> None:
        """Adds playlist to list"""
        self._playlists.append(playlist)

    def get_playlists(self) -> list[Playlist]:
        """Get all playlists"""
        return self._playlists


def main() -> None:
    track1 = Track(title="False Alarm", artist="The Weeknd", _duration_sec=221)
    track2 = Track(title="MAKING ME SICK!", artist="Terror Reid", _duration_sec=126)

    playlist1 = Playlist("Some music")
    playlist1.add_track(track1)
    playlist1.add_track(track2)

    library = MusicLibrary()
    library.add_playlist(playlist1)

    for playlist in library.get_playlists():
        print(Playlist.format_playlist_info(playlist))


if __name__ == "__main__":
    main()
