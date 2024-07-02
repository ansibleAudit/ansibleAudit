import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


def create_dashboard_ok_failed_rules(pdf, pdf_width, pdf_height, ok_count, failed_count):
    """
    Creates a PDF file that contains a pie chart showing the percentatge of ok and failed rules
    
    Args:
       pdf (PdfPages): PDF object to save the chart.
       pdf_width (float): PDF width
       pdf_height (float): PDF height
       ok_count (int): Number of executed rules successfully (OK)
       failed_count (int): Number of failed rules (FAILED)

    Returns:
        None: The function saves a pdf file on the directory "dashboards"
    """
    # Dashboard 1: Percentage of playbook execution results
    labels = ['OK', 'FAILED']
    sizes = [ok_count, failed_count]
    colors = ['#4CAF50', '#FF0000']
    explode = (0.1, 0)
    # Create the pie chart
    fig1, ax1 = plt.subplots(figsize=(pdf_width, pdf_height))
    ax1.pie(
       sizes, explode=explode,
       labels=labels, colors=colors, shadow=True, startangle=90, autopct='%1.1f%%'
    )
    ax1.axis('equal')
    plt.title('Execution results: OK/FAILED')
    # Save the graph to the PDF
    pdf.savefig(fig1)
    plt.close()
    
    
def create_dashboard_vulnerability_severities(pdf, pdf_width, pdf_height, rating_counts):
    """
    Creates a bar chart showing the count of different vulnerability severities
    
    Args:
       pdf (PdfPages): PDF object to save the graphic.
       pdf_width (float): PDF width
       pdf_height (float): PDF height
       rating_counts (dict): Represents a vulnerability severity level and the vulnerability count for that level.
    Returns:
        
    """
    # Dashboard 2: Count of vulneraiblity categories
    categories = ['None', 'Low', 'Medium', 'High', 'Critical']
    counts = []
    for category in categories:
       counts.append(rating_counts.get(category, 0))
    fig2, ax2 = plt.subplots(figsize=(pdf_width, pdf_height))
    ax2.bar(
       categories, counts, color=['#808080', '#4CAF50', '#FFEB3B', '#FF9800', '#F44336']
    )
    ax2.set_xlabel('Vulnerability Severity')
    ax2.set_ylabel('Count')
    ax2.set_title('Vulnerability Severities')
    ax2.grid(True, axis='y') 
    ax2.yaxis.set_major_locator(plt.MaxNLocator(integer=True))       
    pdf.savefig(fig2)
    plt.close()
    
    
def create_pdf_with_dashboards(ok_count, failed_count, total_rules_checked, rating_counts):
    """
    Creates a PDF file that contains a pie chart that shows the percentage of playbook execution results.

    Args:
        ok_count (int): Number of rules executed successfully (OK).
        failed_count (int): Number of rules that failed execution.
        total_rules_checked (int): Total number of rules checked 
        rating_counts (dict): Represents a vulnerability severity level and the vulnerability count for that level.

    Returns:
        None: The function saves a PDF file in the "dashboards" directory.
    """
    # PDF size
    pdf_width, pdf_height = 8, 6
    # Create a PDF file
    with PdfPages("dashboards/dashboards.pdf") as pdf:
        create_dashboard_ok_failed_rules(pdf, pdf_width, pdf_height, ok_count, failed_count)
        create_dashboard_vulnerability_severities(pdf, pdf_width, pdf_height, rating_counts)
