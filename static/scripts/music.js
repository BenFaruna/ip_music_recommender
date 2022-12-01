const playerButton = document.querySelector('.player-button'),
      audio = document.querySelector('audio'),
      timeline = document.querySelector('.timeline'),
      soundButton = document.querySelector('.sound-button'),
  
      pauseIcon = '<i class="bi bi-pause-fill"></i>',
      playIcon = '<i class="bi bi-play-fill"></i>',
      soundIcon = '<i class="bi bi-volume-up-fill"></i>',
      muteIcon = '<i class="bi bi-volume-mute-fill"></i>';

function toggleAudio () {
  if (audio.getAttribute('src') == null) {
    alert('No preview url')
    return;
  }

  if (audio.paused) {
    audio.play();
    playerButton.innerHTML = pauseIcon;
  } else {
    audio.pause();
    playerButton.innerHTML = playIcon;
  }
}

playerButton.addEventListener('click', toggleAudio);

// function changeTimelinePosition () {
//   const percentagePosition = (100*audio.currentTime) / audio.duration;
//   timeline.style.backgroundSize = `${percentagePosition}% 100%`;
//   timeline.value = percentagePosition;
//   $('#seek').attr('value', percentagePosition);
// }

// audio.ontimeupdate = changeTimelinePosition;

function audioEnded () {
  playerButton.innerHTML = playIcon;
}

audio.onended = audioEnded;

// function changeSeek () {
//   const time = (timeline.value * audio.duration) / 100;
//   audio.currentTime = time;
// }

// timeline.addEventListener('change', changeSeek);

function toggleSound () {
  audio.muted = !audio.muted;
  soundButton.innerHTML = audio.muted ? muteIcon : soundIcon;
}

soundButton.addEventListener('click', toggleSound);
