clear all
clc

num_files=6;
num_steps=20;
size_Vi=609;

V=zeros(num_steps,num_steps,num_files);
Vn=zeros(num_steps,num_steps,num_files);
Vi=zeros(size_Vi,size_Vi,num_files);

for n = 1:num_files
    i=n-1;
    m=1;
    a=csvread("4H_5s_scan_"+i+".csv");
    Z=a(:,3)';
    for j = 1:num_steps
        for k = 1:num_steps
            V(j,k,n)=Z(m);
            m=m+1;
        end
    end
end

min = min([V(:)']);
max = max([V(:)']);
fig = figure(1);

for m = 1:num_files
    Vn(:,:,m)=(V(:,:,m)-min)/(max-min);
    Vi(:,:,m) = interp2(Vn(:,:,m),5,'cubic');
    Vi_size = size(Vi,1);
    subplot(ceil(sqrt(num_files)),ceil(sqrt(num_files)),m)
    pcolor(Vi(:,:,m));
    xticks([1,Vi_size]);
    xticklabels({'0', '20'});
    yticks([1,Vi_size]);
    yticklabels({'0', '20'});
    xlabel({'X (\mum)'});
    y=ylabel('Y (\mum)', 'Rotation',0);
    y.Position(1) = -60;
    title(sprintf('V 4H-SiC Scan %d',m))
    shading interp;
end

h = axes(fig, 'visible', 'off');
cb = colorbar(h,'Position',[0.92 0.168 0.022 0.7]);
cb.Label.String = {'PL','Norm.'};
cb.Label.Position = [0.7 1.1];
cb.Label.Rotation = 0;
cb.Label.FontWeight = 'bold'
caxis(h,[0,1]);

