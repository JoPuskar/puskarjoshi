        // Get all links with an ID that starts with 'sectionLink'
        const sectionLinks = document.querySelectorAll('a[href^="#"]');

        // Loop through all section links
        sectionLinks.forEach(sectionLink => {
          sectionLink.addEventListener('click', event => {
            // Prevent default behavior
            event.preventDefault();

            // Get the target section based on the href attribute of the link
            const targetSection = document.querySelector(sectionLink.getAttribute('href'));

            // Scroll to the target section using smooth behavior
            targetSection.scrollIntoView({
              behavior: 'smooth'
            });
          });
        });