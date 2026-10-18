/**
 * Smart Quiz - Main JavaScript
 * Handles:
 * - Active navbar heading selection for Home vs Categories
 * - Scrollspy navigation
 * - Category card selection & modal title synchronization
 * - Student name caching via localStorage
 * - Live filter/search on history/leaderboard page
 */

document.addEventListener("DOMContentLoaded", () => {
  // Modal elements
  const studentModal = document.getElementById("studentNameModal");
  const modalCloseBtn = document.getElementById("modalCloseBtn");
  const modalCancelBtn = document.getElementById("modalCancelBtn");
  const startQuizForm = document.getElementById("startQuizForm");
  const studentNameInput = document.getElementById("studentNameInput");
  const selectedCategoryNameSpan = document.getElementById("selectedCategoryName");

  // Navbar elements
  const navLinkHome = document.getElementById("nav-link-home");
  const navLinkCategories = document.getElementById("nav-link-categories");
  const categoriesSection = document.getElementById("categories");

  // Mobile Hamburger Menu Elements
  const mobileNavToggle = document.getElementById("mobileNavToggle");
  const navMenu = document.getElementById("navMenu");

  function toggleMobileMenu() {
    if (!mobileNavToggle || !navMenu) return;
    const isExpanded = mobileNavToggle.classList.toggle("active");
    navMenu.classList.toggle("active");
    mobileNavToggle.setAttribute("aria-expanded", isExpanded);
  }

  function closeMobileMenu() {
    if (!mobileNavToggle || !navMenu) return;
    mobileNavToggle.classList.remove("active");
    navMenu.classList.remove("active");
    mobileNavToggle.setAttribute("aria-expanded", "false");
  }

  if (mobileNavToggle) {
    mobileNavToggle.addEventListener("click", (e) => {
      e.stopPropagation();
      toggleMobileMenu();
    });
  }

  // Close mobile menu when any nav item is clicked
  const navLinks = document.querySelectorAll(".nav-menu .nav-item a");
  navLinks.forEach(link => {
    link.addEventListener("click", closeMobileMenu);
  });

  // Close menu when clicking outside
  document.addEventListener("click", (e) => {
    if (navMenu && navMenu.classList.contains("active")) {
      if (!navMenu.contains(e.target) && !mobileNavToggle.contains(e.target)) {
        closeMobileMenu();
      }
    }
  });

  // -------------------------------------------------------------
  // 1. Navbar Active Heading Switching & Scrollspy
  // -------------------------------------------------------------
  function setActiveNavHeading(linkToActivate) {
    if (navLinkHome) navLinkHome.classList.remove("active");
    if (navLinkCategories) navLinkCategories.classList.remove("active");
    if (linkToActivate) linkToActivate.classList.add("active");
  }

  // Check URL hash on initial load
  if (window.location.hash === "#categories") {
    setActiveNavHeading(navLinkCategories);
  }

  // Navbar Click: Categories
  if (navLinkCategories) {
    navLinkCategories.addEventListener("click", () => {
      setActiveNavHeading(navLinkCategories);
      closeMobileMenu();
    });
  }

  // Navbar Click: Home
  if (navLinkHome) {
    navLinkHome.addEventListener("click", (e) => {
      const isHomePage = (window.location.pathname === "/" || window.location.pathname === "");
      if (isHomePage) {
        setActiveNavHeading(navLinkHome);
      }
    });
  }

  // Scrollspy: update active heading as student scrolls on the home page
  if (categoriesSection && navLinkHome && navLinkCategories) {
    let scrollTimeout;
    window.addEventListener("scroll", () => {
      clearTimeout(scrollTimeout);
      scrollTimeout = setTimeout(() => {
        const rect = categoriesSection.getBoundingClientRect();
        // If categories section has entered the viewport
        if (rect.top <= 200 && rect.bottom >= 150) {
          setActiveNavHeading(navLinkCategories);
        } else if (window.scrollY < 300) {
          setActiveNavHeading(navLinkHome);
        }
      }, 30);
    }, { passive: true });
  }

  // -------------------------------------------------------------
  // 2. Category Card Selection & Modal Heading Sync
  // -------------------------------------------------------------
  const savedName = localStorage.getItem("smart_quiz_student_name");
  if (savedName && studentNameInput) {
    studentNameInput.value = savedName;
  }

  function selectCategoryAndOpenModal(categoryId, categoryName, cardElement) {
    // Visually mark category card as selected
    document.querySelectorAll(".category-card").forEach(c => c.classList.remove("card-selected"));
    if (cardElement) {
      cardElement.classList.add("card-selected");
    }

    // Update form action and modal title heading with selected category name
    if (startQuizForm) {
      startQuizForm.action = `/start-quiz/${categoryId}`;
    }
    if (selectedCategoryNameSpan) {
      selectedCategoryNameSpan.textContent = categoryName;
    }

    // Also highlight "Categories" in navbar heading since student is interacting with categories
    setActiveNavHeading(navLinkCategories);

    // Show modal
    if (studentModal) {
      studentModal.classList.add("active");
      setTimeout(() => {
        if (studentNameInput) studentNameInput.focus();
      }, 100);
    }
  }

  // Make entire category cards and their buttons clickable
  const categoryCards = document.querySelectorAll(".category-card");
  categoryCards.forEach(card => {
    const btn = card.querySelector(".btn-open-quiz-modal");
    if (!btn) return;
    const catId = btn.getAttribute("data-category-id");
    const catName = btn.getAttribute("data-category-name");

    // Clicking anywhere on the card
    card.addEventListener("click", (e) => {
      selectCategoryAndOpenModal(catId, catName, card);
    });

    // Clicking button directly
    btn.addEventListener("click", (e) => {
      e.stopPropagation();
      selectCategoryAndOpenModal(catId, catName, card);
    });
  });

  // Close modal
  function closeModal() {
    if (studentModal) {
      studentModal.classList.remove("active");
    }
    // Remove card selected glow when modal is dismissed
    document.querySelectorAll(".category-card").forEach(c => c.classList.remove("card-selected"));
  }

  if (modalCloseBtn) modalCloseBtn.addEventListener("click", closeModal);
  if (modalCancelBtn) modalCancelBtn.addEventListener("click", closeModal);

  if (studentModal) {
    studentModal.addEventListener("click", (e) => {
      if (e.target === studentModal) {
        closeModal();
      }
    });
  }

  // Save student name to localStorage upon submission
  if (startQuizForm) {
    startQuizForm.addEventListener("submit", (e) => {
      const nameVal = studentNameInput.value.trim();
      if (!nameVal) {
        e.preventDefault();
        alert("Please enter your name to proceed.");
        studentNameInput.focus();
        return;
      }
      localStorage.setItem("smart_quiz_student_name", nameVal);
    });
  }

  // -------------------------------------------------------------
  // 3. Live Filter / Search on History / Leaderboard Page
  // -------------------------------------------------------------
  const searchInput = document.getElementById("historySearchInput");
  const historyRows = document.querySelectorAll(".history-data-row");

  if (searchInput && historyRows.length > 0) {
    searchInput.addEventListener("input", () => {
      const query = searchInput.value.toLowerCase().trim();
      historyRows.forEach(row => {
        const student = (row.getAttribute("data-student") || "").toLowerCase();
        const category = (row.getAttribute("data-category") || "").toLowerCase();
        if (student.includes(query) || category.includes(query)) {
          row.style.display = "";
        } else {
          row.style.display = "none";
        }
      });
    });
  }
});
