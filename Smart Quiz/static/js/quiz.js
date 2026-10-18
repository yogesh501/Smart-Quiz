/**
 * Smart Quiz - Interactive Quiz Engine
 * Features:
 * - Slide navigation (Next, Prev, Palette jump)
 * - Single option selection with instant feedback
 * - Visual progress tracking & answered question counter
 * - Pre-submission confirmation summary (answered vs unanswered)
 * - Server-side validation and secure score calculation
 */

document.addEventListener("DOMContentLoaded", () => {
  const slides = document.querySelectorAll(".question-slide");
  const totalQuestions = slides.length;
  if (totalQuestions === 0) return;

  let currentIndex = 0;
  const userAnswers = {}; // Map: { question_id: 'A' | 'B' | 'C' | 'D' }

  // Elements
  const prevBtn = document.getElementById("prevBtn");
  const nextBtn = document.getElementById("nextBtn");
  const submitBtn = document.getElementById("submitBtn");
  const questionCounter = document.getElementById("questionCounter");
  const progressBarFill = document.getElementById("progressBarFill");
  const paletteBtns = document.querySelectorAll(".palette-btn");

  // Confirmation Modal Elements
  const submitConfirmModal = document.getElementById("submitConfirmModal");
  const confirmAnsweredCount = document.getElementById("confirmAnsweredCount");
  const confirmUnansweredCount = document.getElementById("confirmUnansweredCount");
  const cancelSubmitBtn = document.getElementById("cancelSubmitBtn");
  const finalSubmitBtn = document.getElementById("finalSubmitBtn");
  const quizForm = document.getElementById("quizForm");

  // Function to show specific question slide
  function showSlide(index) {
    if (index < 0 || index >= totalQuestions) return;
    
    slides.forEach((slide, idx) => {
      slide.classList.toggle("active", idx === index);
    });

    currentIndex = index;

    // Update Counter (e.g. "Question 3 of 10")
    if (questionCounter) {
      questionCounter.textContent = `Question ${currentIndex + 1} of ${totalQuestions}`;
    }

    // Update Progress Bar
    const progressPercent = Math.round(((currentIndex + 1) / totalQuestions) * 100);
    if (progressBarFill) {
      progressBarFill.style.width = `${progressPercent}%`;
    }

    // Update Palette Buttons Active state
    paletteBtns.forEach((btn, idx) => {
      btn.classList.toggle("active", idx === currentIndex);
    });

    // Update Navigation Buttons visibility
    if (prevBtn) {
      prevBtn.disabled = (currentIndex === 0);
    }
    if (nextBtn) {
      nextBtn.style.display = (currentIndex === totalQuestions - 1) ? "none" : "inline-flex";
    }
    if (submitBtn) {
      submitBtn.style.display = (currentIndex === totalQuestions - 1) ? "inline-flex" : "none";
    }
  }

  // Handle Option Click
  const optionItems = document.querySelectorAll(".option-item");
  optionItems.forEach(item => {
    item.addEventListener("click", () => {
      const qId = item.getAttribute("data-question-id");
      const optLetter = item.getAttribute("data-option-letter");

      // Deselect siblings in the same question
      const siblingOptions = document.querySelectorAll(`.option-item[data-question-id="${qId}"]`);
      siblingOptions.forEach(sib => sib.classList.remove("selected"));

      // Select clicked option
      item.classList.add("selected");
      userAnswers[qId] = optLetter;

      // Update hidden input if present in form
      const hiddenInput = document.getElementById(`input_q_${qId}`);
      if (hiddenInput) {
        hiddenInput.value = optLetter;
      }

      // Mark bubble in palette as answered
      const currentPaletteBtn = document.getElementById(`palette_btn_${currentIndex}`);
      if (currentPaletteBtn) {
        currentPaletteBtn.classList.add("answered");
      }
    });
  });

  // Next Button Click
  if (nextBtn) {
    nextBtn.addEventListener("click", () => {
      if (currentIndex < totalQuestions - 1) {
        showSlide(currentIndex + 1);
      }
    });
  }

  // Previous Button Click
  if (prevBtn) {
    prevBtn.addEventListener("click", () => {
      if (currentIndex > 0) {
        showSlide(currentIndex - 1);
      }
    });
  }

  // Question Palette Bubble Jump
  paletteBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      const targetIndex = parseInt(btn.getAttribute("data-index"), 10);
      if (!isNaN(targetIndex)) {
        showSlide(targetIndex);
      }
    });
  });

  // Open Submission Confirmation Modal
  function openConfirmModal() {
    const answeredCount = Object.keys(userAnswers).length;
    const unansweredCount = totalQuestions - answeredCount;

    if (confirmAnsweredCount) confirmAnsweredCount.textContent = answeredCount;
    if (confirmUnansweredCount) confirmUnansweredCount.textContent = unansweredCount;

    if (submitConfirmModal) {
      submitConfirmModal.classList.add("active");
    }
  }

  function closeConfirmModal() {
    if (submitConfirmModal) {
      submitConfirmModal.classList.remove("active");
    }
  }

  if (submitBtn) {
    submitBtn.addEventListener("click", openConfirmModal);
  }

  if (cancelSubmitBtn) {
    cancelSubmitBtn.addEventListener("click", closeConfirmModal);
  }

  if (submitConfirmModal) {
    submitConfirmModal.addEventListener("click", (e) => {
      if (e.target === submitConfirmModal) {
        closeConfirmModal();
      }
    });
  }

  // Final Submit Action
  if (finalSubmitBtn) {
    finalSubmitBtn.addEventListener("click", () => {
      finalSubmitBtn.disabled = true;
      finalSubmitBtn.textContent = "Calculating Score...";

      // Send answers via fetch API for smooth transition
      fetch("/submit-quiz", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          answers: userAnswers
        })
      })
      .then(res => res.json())
      .then(data => {
        if (data.success && data.redirect_url) {
          window.location.href = data.redirect_url;
        } else {
          alert("Submission error: " + (data.error || "Please try again."));
          finalSubmitBtn.disabled = false;
          finalSubmitBtn.textContent = "Yes, Submit Quiz";
        }
      })
      .catch(err => {
        console.error("Submission failed:", err);
        // Fallback to traditional form submission
        if (quizForm) {
          quizForm.submit();
        } else {
          alert("Network error submitting quiz. Please check connection.");
          finalSubmitBtn.disabled = false;
          finalSubmitBtn.textContent = "Yes, Submit Quiz";
        }
      });
    });
  }

  // Initialize with the first question
  showSlide(0);
});
