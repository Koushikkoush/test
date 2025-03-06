from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from lead.models import Lead
from client.models import Client
from team.models import Team

@login_required
# Add this to your views.py

def dashboard(request):
    team = request.user.userprofile.active_team
    
    # Get leads and clients
    leads = Lead.objects.filter(team=team, converted_to_client=False).order_by('-created_at')[:5]
    clients = Client.objects.filter(team=team).order_by('-created_at')[:5]
    
    # Get lead counts by status
    contacted_leads_count = Lead.objects.filter(team=team, status=Lead.CONTACTED).count()
    won_leads_count = Lead.objects.filter(team=team, status=Lead.WON).count()
    lost_leads_count = Lead.objects.filter(team=team, status=Lead.LOST).count()
    
    return render(request, 'dashboard/dashboard.html', {
        'leads': leads,
        'clients': clients,
        'contacted_leads_count': contacted_leads_count,
        'won_leads_count': won_leads_count,
        'lost_leads_count': lost_leads_count,
    })