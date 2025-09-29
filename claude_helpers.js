// Helper functions for Claude.ai conversation imports

module.exports = {
  // Format dates consistently - simplified version
  formatDate: function(dateString) {
    if (!dateString) return 'Unknown Date';
    
    try {
      const date = new Date(dateString);
      if (isNaN(date.getTime())) return 'Unknown Date';
      
      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, '0');
      const day = String(date.getDate()).padStart(2, '0');
      
      return `${year}-${month}-${day}`;
    } catch (error) {
      return 'Unknown Date';
    }
  },

  // Equality check for conditionals
  eq: function(a, b) {
    return a === b;
  }
};